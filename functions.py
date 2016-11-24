import sys
from stack import *

# Stack Manipulation / IO:
def take_input(stack):
    stack.push(eval(input()))
def take_raw_input(stack):
    stack.push(input())
def take_raw_input_split_newlines(stack):
    stack.push(sys.stdin.read().split('\n'))
def take_raw_input_split_spaces(stack):
    stack.push(sys.stdin.read().split(' '))
def take_raw_input_split_delim(stack):
    stack.push(sys.stdin.read().split(str(stack.pop())))
