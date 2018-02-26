import os
import argparse
from .stack import *
from .functionsdict import *

def process(tokens, past_stack=None):
    stack = past_stack
    if not stack:
        stack = Stack()
    index = 0
    while 0 <= index < len(tokens):
        if tokens[index] in chord_functions.keys():
            chord_functions[tokens[index]](stack)
        index += 1
    print(stack)
    return stack

def readf(path, lyrics):
    prog = ''
    with open(path, 'r') as file:
        prog = file.read()
    prog = prog.split('\n')
    if lyrics:
        prog = prog[::2]
    prog = [x.split() for x in prog]
    tokens = []
    for row in prog:
        tokens += row
    process(tokens)

def replenv():
    inp = input("td> ")
    cstack = Stack()
    while inp != "quit":
        cstack = process(inp.split(), cstack)
        inp = input("td> ")

def main():
    parser = argparse.ArgumentParser(description = 'Interpreter for the tone-deaf programming language.')
    parser.add_argument('-f', type=str, help='Open a tone-deaf source file.')
    parser.add_argument('-l', action='store_true', help='Open the source file in "lyric mode".')
    args = parser.parse_args()
    if args.f != None:
        if args.f != '':
            if os.path.isfile(args.f):
                readf(args.f, args.l)
            else:
                print('-f: Error - no path given.')
        else:
            print('-f: Error - no path given.')
    else:
        replenv()

if __name__ == '__main__':
    main()
