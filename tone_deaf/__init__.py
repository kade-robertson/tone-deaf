import os
import argparse
from .stack import *
from .chords import all_chords

def trycast(token):
    try:
        return int(token)
    except ValueError:
        pass
    try:
        return float(token)
    except ValueError:
        pass
    return None

def process(tokens, past_stack=None):
    stack = past_stack
    if not stack:
        stack = Stack()
    index = 0
    while 0 <= index < len(tokens):
        if tokens[index] in all_chords.keys():
            all_chords[tokens[index]](stack)
        if tokens[index].startswith('|'):
            st = tokens[index][1:]
            if st.endswith('|') and not st.endswith(r'\|'):
                st = st[:-1]
            else:
                index += 1
                while index < len(tokens):
                    st += " " + tokens[index]
                    if tokens[index].endswith('|') and not tokens[index].endswith(r'\|'):
                        st = st[:-1]
                        break
                    elif tokens[index].endswith(r'\|'):
                        st = st[:-2] + "|"
                    index += 1
            stack.push(st)
        else:
            casted = trycast(tokens[index])
            if casted is not None:
                stack.push(casted)
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
