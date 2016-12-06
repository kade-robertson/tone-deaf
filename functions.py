import sys
from stack import *

# Used by one of the chords, previously unimplemented:
def tetrate(x, y):
    out = x
    while y > 1:
        out = x ** out
        y -= 1
    return out
def is_prime(x):
    if x % 2 == 0 or x < 2:
        return 0
    elif x == 2:
        return 1
    else:
        i = 3
        while i < int(x**.5)+1:
            if x % i == 0:
                return 0
            i += 2
        return 1

# [A Chords] Math Operations:
def pop_2_and_add(stack):
    stack.push(stack.pop() + stack.pop())
def pop_2_and_subtr(stack):
    a = stack.pop()
    stack.push(stack.pop() - a)
def pop_2_and_mult(stack):
    stack.push(stack.pop() * stack.pop())
def pop_2_and_divd(stack):
    a = stack.pop()
    stack.push(stack.pop() / a)
def pop_2_and_modul(stack):
    a = stack.pop()
    stack.push(stack.pop() % a)
def pop_and_square(stack):
    a = stack.pop()
    stack.push(a * a)
def pop_and_cube(stack):
    a = stack.pop()
    stack.push(a * a * a)
def pop_and_sqrt(stack):
    stack.push(stack.pop() ** 0.5)
def pop_and_cbrt(stack):
    stack.push(stack.pop() ** (1/3))
def pop_2_and_exp(stack):
    a = stack.pop()
    stack.push(stack.pop() ** a)
def pop_2_and_tetr(stack):
    a = stack.pop()
    stack.push(tetrate(stack.pop(), a))
def pop_2_and_check_greater(stack):
    a = stack.pop()
    stack.push(1 if stack.pop() > a else 0)
def pop_2_and_check_greq(stack):
    a = stack.pop()
    stack.push(1 if stack.pop() >= a else 0)
def pop_and_check_parity(stack):
    stack.push(stack.pop()%2)
def pop_and_check_primality(stack):
    stack.push(is_prime(stack.pop()))

# [E Chords] Stack Manipulation / IO:
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
