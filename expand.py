#!/usr/bin/env python3

def Expand(fname):
    print("TODO: Expand " + fname)

def Unexpand(fname):
    print("TODO: Unexpand " + fname)

def req_code(msg, valid):
    """Repeatedly ask for input until one of the valid answers is recieved
    msg: A message to repeatedly display the user to prompt for an answer
    valid: a list of valid responses"""
    response = ""
    while not response in valid:
        response = input(msg).lower()
    return response

functs  = dict({"e": Expand, "u": Unexpand})

if __name__ == "__main__":
    while True:
        mode = req_code("Expand (e) or Unexpand (u) a file: ", functs.keys())
        fname = input("Enter filename: ")
        functs[mode](fname)
