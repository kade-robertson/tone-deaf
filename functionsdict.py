from functions import *

# E chords are used for stack manipulation and I/O.
e_chords = { 'E' : take_input,
             'Em': take_raw_input,
             'E5': take_raw_input_split_newlines,
             'E6': take_raw_input_split_spaces,
             'E7': take_raw_input_split_delim }

chord_functions = dict(list(e_chords.items()))
