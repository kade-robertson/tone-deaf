# tone-deaf

tone-deaf is an esoteric programming language which manipulates a stack based on chords. This repository contains a reference interpreter for the language as well as the wiki describing each function.

tone-deaf can be installed through `pip`:

```
pip install tone-deaf
```

# Running from a file

Programs can be run from a file in one of two modes: normal or 'lyric' mode. Lyric mode allows you to leave comments on every other line, like so:

```
E E E
The above takes 3 integers.
A7 A7
This will calculate (a ** (b ** c)).
```

which the intepreter reads as:

```
E E E A7 A7
```

Normal mode assumes there are no comments. To load a file in normal mode, use the `-f` switch, i.e. `tone-deaf -f program.deaf`. To load a file in lyric mode, use the `-l` switch, i.e. `tone-deaf -l program.deaf`.

# Using the REPL

If no file is provided via the switches above, you will be provided with a REPL. This will work the same was as the paring for normal files would, except the stack is persistent throughout the entire execution. Example:

```
td> E E E
1
2
3
[1 2 3]
td> Em7
[1 2 3 3]
td> E7#9
[3 3 2 1]
td> A7 A7 A7
[19683]
td> quit
...
```

The stack will be printed out after each line entered.