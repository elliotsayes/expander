#!/usr/bin/env python3
import sys
import os

write_expansion_code = 8

source_base_dir = "files/examples/"
expanded_base_dir = "files/expanded/"
unexpanded_base_dir = "files/unexpanded/"

def expand_byte(byte_in, ex_code):
    n_bytes = 2**ex_code
    bytes_out = bytearray(n_bytes)
    bytes_out[:-1] = os.urandom(n_bytes-1)

    byte_sum = 0
    for b in bytes_out:
        byte_sum += b
    bytes_out[-1] = (byte_in[0] - byte_sum) % 256

    return bytes_out

def unexpand_byte(bytes):
    print("TODO")

def path_check():
    paths = [source_base_dir, expanded_base_dir, unexpanded_base_dir]
    for path in paths:
        if not os.path.exists(path):
            os.makedirs(path)

def expand_file(fname):
    print("TODO: Expand " + fname)

    fname_in = os.path.join(source_base_dir,fname)
    fname_out = os.path.join(expanded_base_dir,fname)

    with open(fname_in, 'rb') as fo_in, open(fname_out, 'wb') as fo_out:
        fo_out.write(bytes([write_expansion_code]))

        byte = fo_in.read(1)
        while byte:
            expanded_byte = expand_byte(byte, write_expansion_code)
            fo_out.write(expanded_byte)
            byte = fo_in.read(1)

def unexpand_file(fname):
    print("TODO: Unexpand " + fname)

def req_code(msg, valid):
    """Repeatedly ask for input until one of the valid answers is recieved
    msg: A message to repeatedly display the user to prompt for an answer
    valid: a list of valid responses"""
    response = ""
    while not response in valid:
        response = input(msg).lower()
    return response

def print_help():
    print("""Usage: expand.py [-h] [-e <filename> N | -u <filename>]
-h : show this help
-e : expand file
-u : unexpand file""")

def interactive():
    while True:
        mode = req_code("Expand (e) or Unexpand (u) a file: ", functs.keys())
        fname = input("Enter filename: ")
        functs[mode](fname)

functs  = dict({"e": expand_file, "u": unexpand_file})

if __name__ == "__main__":
    path_check()
    if len(sys.argv) is 1:
        interactive()
    else:
        try:
            command = sys.argv[1][1:]
            fname = sys.argv[2]
            functs[command](fname)
        except (IndexError, KeyError):
            print_help()
