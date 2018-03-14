# E Chords perform stack manipulation.

import sys

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

def take_raw_input_split_comma(stack):
    stack.push(sys.stdin.read().split(','))

def pop_2_and_swap(stack):
    b = stack.pop()
    a = stack.pop()
    stack.push(b)
    stack.push(a)

def pop_and_discard(stack):
    stack.pop()

def pop_and_push_twice(stack):
    item = stack.pop()
    stack.push(item)
    stack.push(item)

def pop_and_push_thrice(stack):
    item = stack.pop()
    stack.push(item)
    stack.push(item)
    stack.push(item)

def rotate_stack_right(stack):
    stack.rotate(1)

def rotate_stack_left(stack):
    stack.rotate(-1)

def reverse_stack(stack):
    stack.reverse()

def shuffle_stack(stack):
    stack.shuffle()

def swap_first_and_third(stack):
    c = stack.pop()
    b = stack.pop()
    a = stack.pop()
    stack.push(c)
    stack.push(b)
    stack.push(a)

def pop_under_first(stack):
    stack.pop(-2)

def pop_two_under_first(stack):
    stack.pop(-3)
    stack.pop(-2)

def sort_stack(stack):
    stack.sort()

def sort_stack_desc(stack):
    stack.sort(False)

def swap_first_and_fourth(stack):
    d = stack.pop()
    c = stack.pop()
    b = stack.pop()
    a = stack.pop()
    stack.push(d)
    stack.push(b)
    stack.push(c)
    stack.push(a)

chords = { 
    'E'    : take_input,
    'Em'   : take_raw_input,
    'E5'   : take_raw_input_split_newlines,
    'E6'   : take_raw_input_split_spaces,
    'E7'   : take_raw_input_split_delim,
    'E9'   : take_raw_input_split_comma,
    'Es'   : pop_2_and_swap,
    'Em6'  : pop_and_discard,
    'Em7'  : pop_and_push_twice,
    'EM7'  : pop_and_push_thrice,
    'E11'  : rotate_stack_right,
    'Es4'  : rotate_stack_left,
    'E7#9' : reverse_stack,
    'E75b' : shuffle_stack,
    'E7b9' : swap_first_and_third,
    'Eb^9' : pop_under_first,
    'Em^9' : pop_two_under_first,
    'Ems4' : sort_stack,
    'Em/B' : sort_stack_desc,
    'Em/D' : swap_first_and_fourth
}

__all__ = [ "chords" ]
