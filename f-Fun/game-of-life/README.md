# Game of Life
## Python3 Script Version by Ex10is0n
### How to Use

Easily type `python3 game-of-life.py [life file]` or `python3 game-of-life.py` in the shell

Mentions that the second command to open `game-of-life` needs `vim` installed

```
$ python3 game-of-life.py [life file]

# such as

$ python3 game-of-life.py test1.life
Game of Life Simulator (Version 0.1)
Type "help" to open manual, "q" to exit

Loading file: test1.life
File loaded success
Printing initialized pattern ...
⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️
⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️
⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️
⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️
⬜️⬜️⬜️⬜️⬛️⬛️⬛️⬛️⬛️⬛️⬜️⬛️⬛️⬜️⬜️⬜️⬜️
⬜️⬜️⬜️⬜️⬛️⬛️⬛️⬛️⬛️⬛️⬜️⬛️⬛️⬜️⬜️⬜️⬜️
⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬛️⬛️⬜️⬜️⬜️⬜️
⬜️⬜️⬜️⬜️⬛️⬛️⬜️⬜️⬜️⬜️⬜️⬛️⬛️⬜️⬜️⬜️⬜️
⬜️⬜️⬜️⬜️⬛️⬛️⬜️⬜️⬜️⬜️⬜️⬛️⬛️⬜️⬜️⬜️⬜️
⬜️⬜️⬜️⬜️⬛️⬛️⬜️⬜️⬜️⬜️⬜️⬛️⬛️⬜️⬜️⬜️⬜️
⬜️⬜️⬜️⬜️⬛️⬛️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️
⬜️⬜️⬜️⬜️⬛️⬛️⬜️⬛️⬛️⬛️⬛️⬛️⬛️⬜️⬜️⬜️⬜️
⬜️⬜️⬜️⬜️⬛️⬛️⬜️⬛️⬛️⬛️⬛️⬛️⬛️⬜️⬜️⬜️⬜️
⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️
⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️
⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️
⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️

>
```
### Edit `Life file`

A `life file` is what `game-of-life` runs, if user don't provide, `game-of-life` will create a `life file` by `vim` for you automatically. To edit it, you just follow these grammars:

- Only `0` and `1` seperated by `␣(space)` , to end a line, just simply type `Enter`
- Every Rows and Columns must match, the table must be a `rectangle`
- Do not make any redundant or unessesary chars such as `\n`, `\0`, `␣␣`

The extension of `Life file` is `.life`, it's a plain text file.

### Game-of-life Console Manual

Type `h` in the console to open documentation
```
    Manual Documentations
-------------------------------
Commands:
    r          run single times
    r [int]    run n times
    r inf      keep running

    q          quit

    set [parameters]
        speed  [fast/mid/slow]
        color  [r/g/b/y]

```
