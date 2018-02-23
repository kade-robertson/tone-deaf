from .functions import *

# A chords are used for math operations.
a_chords = { 'A'    : pop_2_and_add,
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
             'A#m7' : pop_2_and_get_comb }

# E chords are used for stack manipulation and I/O.
e_chords = { 'E'    : take_input,
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
             'Em/D' : swap_first_and_fourth }

chord_functions = dict()
chord_functions.update(a_chords)
chord_functions.update(e_chords)
