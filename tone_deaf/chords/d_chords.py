# D Chords are for string / list / set manipulation

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

chords = {
    'D'    : reverse_str,
    'D#'   : shuffle_str,
    'D#4'  : slice_str,
    'D#7'  : slice_str_adv,
    'D#m'  : keep_every_other,
    'D#m7' : keep_every_third,
    'D#M7' : keep_every_fifth,
    'D^9'  : cast_to_set,
    'Dm7'  : palindromize,
    'Dm9'  : is_palindrome
}

__all__ = [ "chords" ]
