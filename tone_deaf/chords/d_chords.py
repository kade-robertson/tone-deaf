# D Chords are for string / list / set manipulation

import itertools
from random import shuffle

def reverse_str(stack):
    s = stack.pop()
    stack.push(s[::-1])

def shuffle_str(stack):
    s = stack.pop()
    if isinstance(s, str):
        s = list(s)
        shuffle(s)
        s = ''.join(s)
    else:
        shuffle(s)
    stack.push(s)

def slice_str(stack):
    end = stack.pop()
    start = stack.pop()
    s = stack.pop()
    end = len(s) if end == 0 else end
    start = 0 if start == 0 else start
    stack.push(s[start:end])

def slice_str_adv(stack):
    skip = stack.pop()
    end = stack.pop()
    start = stack.pop()
    s = stack.pop()
    skip = 1 if skip == 0 else skip
    end = len(s) if end == 0 else end
    start = 0 if start == 0 else start
    stack.push(s[start:end:skip])

def keep_every_other(stack):
    s = stack.pop()
    if isinstance(s, int):
        v = stack.pop()
        stack.push(v[s::2])
    else:
        stack.push(s[::2])

def keep_every_third(stack):
    s = stack.pop()
    if isinstance(s, int):
        v = stack.pop()
        stack.push(v[s::3])
    else:
        stack.push(s[::3])

def keep_every_fifth(stack):
    s = stack.pop()
    if isinstance(s, int):
        v = stack.pop()
        stack.push(v[s::5])
    else:
        stack.push(s[::5])

def cast_to_set(stack):
    s = stack.pop()
    stack.push(set(s))

def palindromize(stack):
    s = stack.pop()
    stack.push(s + s[::-1][1:])

def is_palindrome(stack):
    s = stack.pop()
    stack.push(s == s[::-1])

def interleave_two(stack):
    b = stack.pop()
    a = stack.pop()
    n = None
    if isinstance(a, str) and isinstance(b, str):
        n = ''.join(''.join(x) for x in (list(itertools.zip_longest(a, b, fillvalue = ''))))
    else:
        n = list(itertools.zip_longest(a, b))
    stack.push(n)

def interleave_three(stack):
    c = stack.pop()
    b = stack.pop()
    a = stack.pop()
    n = None
    if isinstance(a, str) and isinstance(b, str) and isinstance(c, str):
        n = ''.join(''.join(x) for x in (list(itertools.zip_longest(a, b, c, fillvalue = ''))))
    else:
        n = list(itertools.zip_longest(a, b, c))
    stack.push(n)

def interleave_n(stack):
    z = stack.pop()
    l = list()
    if z <= 1:
        return
    while z > 0:
        l.insert(0, stack.pop())
        z -= 1
    n = None
    if all(isinstance(x, str) for x in l):
        n = ''.join(''.join(x) for x in (list(itertools.zip_longest(*l, fillvalue = ''))))
    else:
        n = list(itertools.zip_longest(*l))
    stack.push(n)

chords = {
    'D'     : reverse_str,
    'D#'    : shuffle_str,
    'D#4'   : slice_str,
    'D#7'   : slice_str_adv,
    'D#m'   : keep_every_other,
    'D#m7'  : keep_every_third,
    'D#M7'  : keep_every_fifth,
    'D^9'   : cast_to_set,
    'D/A'   : interleave_two,
    'D/B'   : interleave_three,
    'D/C'   : interleave_n,
    'D/C#'  : lambda: None,
    'D/E'   : lambda: None,
    'D/G'   : lambda: None,
    'D11'   : lambda: None,
    'D4'    : lambda: None,
    'D5/E'  : lambda: None,
    'D6'    : lambda: None,
    'D7'    : lambda: None,
    'D7#9'  : lambda: None,
    'D7s2'  : lambda: None,
    'D9^6'  : lambda: None,
    'Dm'    : lambda: None,
    'Dm#7'  : lambda: None,
    'Dm/A'  : lambda: None,
    'Dm/B'  : lambda: None,
    'Dm/C'  : lambda: None,
    'Dm/C#' : lambda: None,
    'Dm7'   : palindromize,
    'Dm9'   : is_palindrome,
    'DM7'   : lambda: None,
    'Ds2'   : lambda: None
}

__all__ = [ "chords" ]
