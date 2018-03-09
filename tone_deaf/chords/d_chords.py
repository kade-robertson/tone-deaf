# D Chords are for string / list manipulation

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
def remove_every_other(stack):
    s = stack.pop(stack)
    stack.push(s[::2])

chords = {
    'D'    : reverse_str,
    'D#'   : shuffle_str,
    'D#4'  : slice_str,
    'D#7'  : slice_str_adv,
    'D#m'  : remove_every_other
}

__all__ = [ "chords" ]
