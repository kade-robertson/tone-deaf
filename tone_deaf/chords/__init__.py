from .a_chords import chords as a_chords
from .d_chords import chords as d_chords
from .e_chords import chords as e_chords

all_chords = dict()
all_chords.update(a_chords)
all_chords.update(d_chords)
all_chords.update(e_chords)

__all__ = [ "all_chords" ]
