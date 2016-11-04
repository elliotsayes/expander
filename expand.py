#!/usr/bin/env python3
import sys
import os

write_expansion_code = 1

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

def expand_file(fname):
    fname_in = os.path.join(source_base_dir,fname)
    fname_out = os.path.join(expanded_base_dir,fname)

    with open(fname_in, 'rb') as fo_in, open(fname_out, 'wb') as fo_out:
        fo_out.write(bytes([write_expansion_code]))
        ratio = 2**write_expansion_code

        byte = fo_in.read(1)
        while byte:
            expanded_byte = expand_byte(byte, ratio)
            fo_out.write(expanded_byte)
            byte = fo_in.read(1)

def unexpand_file(fname):
    fname_in = os.path.join(expanded_base_dir,fname)
    fname_out = os.path.join(unexpanded_base_dir,fname)

    with open(fname_in, 'rb') as fo_in, open(fname_out, 'wb') as fo_out:
        ex_code = fo_in.read(1)
        ratio = 2**ex_code[0]

        byte_sequence = fo_in.read(ratio)
        while byte_sequence:
            unexpanded_byte = unexpand_bytes(byte_sequence)
            fo_out.write(unexpanded_byte)
            byte_sequence = fo_in.read(ratio)

def req_code(msg, valid):
    """Repeatedly ask for input until one of the valid answers is recieved
    msg: A message to repeatedly display the user to prompt for an answer
    valid: a list of valid responses"""
    response = ""
    while not response in valid:
        response = input(msg).lower()
    return response

def print_help():
    print("""Usage: expand.py [-h] [-e <filename> | -u <filename>]
-h : show this help
-e : expand file
-u : unexpand file

Run with no arguments for interactive mode""")

def interactive():
    while True:
        mode = req_code("Expand (e) or Unexpand (u) a file: ", functs.keys())
        fname = input("Enter filename: ")
        functs[mode](fname)

functs  = dict({"e": expand_file, "u": unexpand_file})

def test_byte(n,r):
    e = expand_byte(bytes([n]), r)
    print(e)
    u = unexpand_bytes(e)
    print(u)
    exit()

if __name__ == "__main__":
    path_check()
    #test_byte(0,8)
    if len(sys.argv) is 1:
        interactive()
    else:
        try:
            command = sys.argv[1][1:]
            fname = sys.argv[2]
            functs[command](fname)
        except (IndexError, KeyError):
            print_help()
