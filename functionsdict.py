from functions import *

# A chords are used for math operations.
a_chords = { 'A'   : pop_2_and_add,
             'As'  : pop_2_and_subtr,
             'Am'  : pop_2_and_mult,
             'Ab'  : pop_2_and_divd }

# E chords are used for stack manipulation and I/O.
e_chords = { 'E'   : take_input,
             'Em'  : take_raw_input,
             'E5'  : take_raw_input_split_newlines,
             'E6'  : take_raw_input_split_spaces,
             'E7'  : take_raw_input_split_delim,
             'E9'  : take_raw_input_split_comma,
             'Es'  : pop_2_and_swap,
             'Em6' : pop_and_discard,
             'Em7' : pop_and_push_twice,
             'EM7' : pop_and_push_thrice,
             'E11' : rotate_stack_right,
             'Es4' : rotate_stack_left,
             'E7#9': reverse_stack,
             'E75b': shuffle_stack,
             'E7b9': swap_first_and_third,
             'Eb^9': pop_under_first,
             'Em^9': pop_two_under_first,
             'Ems4': sort_stack,
             'Em/B': sort_stack_desc,
             'Em/D': swap_first_and_fourth }

chord_functions = dict(list(a_chords.items()) + list(e_chords.items()))
