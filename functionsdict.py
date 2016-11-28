from functions import *

# E chords are used for stack manipulation and I/O.
e_chords = { 'E'   : take_input,
             'Em'  : take_raw_input,
             'E5'  : take_raw_input_split_newlines,
             'E6'  : take_raw_input_split_spaces,
             'E7'  : take_raw_input_split_delim,
             'E9'  : take_raw_input_split_comma,
             'Eb'  : swap_first_and_third,
             'Es'  : pop_2_and_swap,
             'Em6' : pop_and_discard,
             'Em7' : pop_and_push_twice,
             'EM7' : pop_and_push_thrice,
             'E11' : rotate_stack_right,
             'Es4' : rotate_stack_left,
             'E7#9': reverse_stack,
             'E75b': shuffle_stack }

chord_functions = dict(list(e_chords.items()))
