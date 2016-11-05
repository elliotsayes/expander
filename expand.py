#!/usr/bin/env python3
import sys
import os

source_base_dir = "files/examples/"
expanded_base_dir = "files/expanded/"
unexpanded_base_dir = "files/unexpanded/"

def path_check():
    paths = [source_base_dir, expanded_base_dir, unexpanded_base_dir]
    for path in paths:
        if not os.path.exists(path):
            os.makedirs(path)

def expand_byte(byte_in, ratio):
    bytes_out = bytearray(ratio)
    bytes_out[:-1] = os.urandom(ratio-1)

    byte_sum = 0
    for b in bytes_out:
        byte_sum += b
    bytes_out[-1] = (byte_in[0] - byte_sum) % 256

    return bytes(bytes_out)

def unexpand_bytes(byte_sequence):
    byte_sum = 0
    for byte in byte_sequence:
        byte_sum += byte
    return bytes([byte_sum % 256])

def expand_file(fname,n):
    fname_in = os.path.join(source_base_dir,fname)
    fname_out = os.path.join(expanded_base_dir,fname)

    try:
        with open(fname_in, 'rb') as fo_in, open(fname_out, 'wb') as fo_out:
            fo_out.write(bytes([n]))
            ratio = 2**n
            print("Expanding with ratio "+str(ratio))

            byte = fo_in.read(1)
            while byte:
                expanded_byte = expand_byte(byte, ratio)
                fo_out.write(expanded_byte)
                byte = fo_in.read(1)
    except FileNotFoundError:
        print("Error: Could not find file: " + fname_in)

def unexpand_file(fname):
    fname_in = os.path.join(expanded_base_dir,fname)
    fname_out = os.path.join(unexpanded_base_dir,fname)

    try:
        with open(fname_in, 'rb') as fo_in, open(fname_out, 'wb') as fo_out:
            ex_code = fo_in.read(1)
            ratio = 2**ex_code[0]
            print("Unexpanding with ratio "+str(ratio))

            byte_sequence = fo_in.read(ratio)
            while byte_sequence:
                unexpanded_byte = unexpand_bytes(byte_sequence)
                fo_out.write(unexpanded_byte)
                byte_sequence = fo_in.read(ratio)
    except FileNotFoundError:
        print("Error: Could not find file: " + fname_in)

def expand_file_int():
    fname = input("File to expand: ")
    n = int(input("Expansion code: "))
    expand_file(fname,n)

def unexpand_file_int():
    fname = input("File to unexpand: ")
    unexpand_file(fname)

def expand_file_cmd(argv):
    try:
        fname = argv[2]
        n = int(argv[3])
        expand_file(fname,n)
    except (IndexError,ValueError):
        print_help()

def unexpand_file_cmd(argv):
    try:
        fname = argv[2]
        unexpand_file(fname)
    except IndexError:
        print_help()

def req_code(msg, valid):
    """Repeatedly ask for input until one of the valid answers is recieved
    msg: A message to repeatedly display the user to prompt for an answer
    valid: a list of valid responses"""
    response = ""
    while not response in valid:
        response = input(msg).lower()
    return response

def print_help():
    print("""Usage: expand.py [-h] [-e <filename> <N> | -u <filename>]
-h : show this help
-e : expand file (N = expansion code)
-u : unexpand file

Run with no arguments for interactive mode""")

int_functs = dict({"e": expand_file_int, "u": unexpand_file_int, "q": exit})
cmd_functs = dict({"-e": expand_file_cmd, "-u": unexpand_file_cmd})

def interactive():
    while True:
        command = req_code("Expand (e) or Unexpand (u) a file (q to quit): ", int_functs.keys())
        int_functs[command]()

def test_byte(n,r):
    e = expand_byte(bytes([n]), r)
    print(e)
    u = unexpand_bytes(e)
    print(u)
    exit()

if __name__ == "__main__":
    path_check()
    #test_byte(0,2)
    if len(sys.argv) is 1:
        interactive()
    else:
        try:
            command = sys.argv[1]
            cmd_functs[command](sys.argv)
        except (IndexError, KeyError):
            print_help()
