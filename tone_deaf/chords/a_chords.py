# A Chords are math operations.

import math
import fractions
from .utils import *

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

def pop_and_get_prime_factors(stack):
    stack.push(prime_factors(stack.pop()))

def pop_3_and_exp_mod(stack):
    a = stack.pop()
    b = stack.pop()
    stack.push(pow(stack.pop(), b, a))

def pop_3_and_tetr_mod(stack):
    a = stack.pop()
    b = stack.pop()
    stack.push(tetr_mod(stack.pop(), b, a))

def pop_and_double(stack):
    stack.push(2 * stack.pop())

def pop_and_halve(stack):
    stack.push(stack.pop() / 2)

def pop_and_round(stack):
    stack.push(round(stack.pop()))

def pop_and_floor(stack):
    stack.push(math.floor(stack.pop()))

def pop_and_ceil(stack):
    stack.push(math.ceil(stack.pop()))

def pop_2_and_divd_int(stack):
    a = stack.pop()
    stack.push(stack.pop() // a)

def pop_2_and_divmod(stack):
    a = stack.pop()
    b = stack.pop()
    stack.push([b // a, b % a])

def pop_2_and_get_gcd(stack):
    a = stack.pop()
    stack.push(fractions.gcd(stack.pop(), a))

def pop_2_and_get_lcm(stack):
    a = stack.pop()
    b = stack.pop()
    stack.push((a*b)/fractions.gcd(a,b))

def pop_and_get_nth_trinum(stack):
    a = stack.pop()
    stack.push((a*-~a)/2)

def pop_2_and_get_perm(stack):
    a = stack.pop()
    b = stack.pop()
    stack.push(math.factorial(b)/math.factorial(b-a))

def pop_2_and_get_comb(stack):
    a = stack.pop()
    b = stack.pop()
    stack.push(math.factorial(b)/(math.factorial(a)*math.factorial(b-a)))

chords = {
    'A'    : pop_2_and_add,
    'As'   : pop_2_and_subtr,
    'Am'   : pop_2_and_mult,
    'Ad'   : pop_2_and_divd,
    'Ab'   : pop_2_and_modul,
    'A+'   : pop_and_square,
    'A#'   : pop_and_cube,
    'A4'   : pop_and_sqrt,
    'A6'   : pop_and_cbrt,
    'A7'   : pop_2_and_exp,
    'A9'   : pop_2_and_tetr,
    'A#4'  : pop_2_and_check_greater,
    'A#7'  : pop_2_and_check_greq,
    'A#d'  : pop_and_check_parity,
    'A#m'  : pop_and_check_primality,
    'A/D'  : pop_and_get_prime_factors,
    'A11'  : pop_3_and_exp_mod,
    'A13'  : pop_3_and_tetr_mod,
    'A7+'  : pop_and_double,
    'AM7'  : pop_and_halve,
    'Ab+'  : pop_and_round,
    'Ab4'  : pop_and_floor,
    'Ab7'  : pop_and_ceil,
    'Abd'  : pop_2_and_divd_int,
    'Abm'  : pop_2_and_divmod,
    'Am6'  : pop_2_and_get_gcd,
    'Am7'  : pop_2_and_get_lcm,
    'Am9'  : pop_and_get_nth_trinum,
    'A#M7' : pop_2_and_get_perm,
    'A#m7' : pop_2_and_get_comb
}

__all__ = [ "chords" ]
