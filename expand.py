#!/usr/bin/env python3
import sys

def expand(fname):
    print("TODO: Expand " + fname)

def unexpand(fname):
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
    print("""Usage: expand.py [-h] [-e <filename> | -u <filename>]
-h : show this help
-e : expand file
-u : unexpand file""")

def interactive():
    while True:
        mode = req_code("Expand (e) or Unexpand (u) a file: ", functs.keys())
        fname = input("Enter filename: ")
        functs[mode](fname)

functs  = dict({"e": expand, "u": unexpand})

if __name__ == "__main__":
    if len(sys.argv) is 1:
        interactive()
    else:
        try:
            command = sys.argv[1][1:]
            fname = sys.argv[2]
            functs[command](fname)
        except (IndexError, KeyError):
            print_help()
