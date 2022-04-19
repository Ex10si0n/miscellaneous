# Common Lisp Learning Note

## Learning Source
![](https://gigamonkeys.com/book/small-cover.gif)
URL: [gigamonkeys/book](https://gigamonkeys.com/book/)

## REPL

Binary: `clisp` can be installed by package manager in UNIX

```bash
brew install clisp
```

Running REPL with `clisp` command

```bash
 clisp
  i i i i i i i       ooooo    o        ooooooo   ooooo   ooooo
  I I I I I I I      8     8   8           8     8     o  8    8
  I  \ `+' /  I      8         8           8     8        8    8
   \  `-+-'  /       8         8           8      ooooo   8oooo
    `-__|__-'        8         8           8           8  8
        |            8     o   8           8     o     8  8
  ------+------       ooooo    8oooooo  ooo8ooo   ooooo   8

Welcome to GNU CLISP 2.49.92 (2018-02-18) <http://clisp.org/>

Copyright (c) Bruno Haible, Michael Stoll 1992-1993
Copyright (c) Bruno Haible, Marcus Daniels 1994-1997
Copyright (c) Bruno Haible, Pierpaolo Bernardi, Sam Steingold 1998
Copyright (c) Bruno Haible, Sam Steingold 1999-2000
Copyright (c) Sam Steingold, Bruno Haible 2001-2018

Type :h and hit Enter for context help.

[1]> 
```

## Emacs
![](https://www.gnu.org/software/emacs/images/emacs.png)

`.emacs` configuration for better usability of clisp.

```lisp
(require 'package)
(add-to-list 'package-archives '("melpa" . "https://melpa.org/packages/") t)
(package-initialize)

(setq inferior-lisp-program "/opt/homebrew/bin/clisp")
```

Installation for SLIME (Lisp REPL in Emacs) see url @ [slime/doc](https://common-lisp.net/project/slime/doc/html/Installation.html)

## Hello World
```bash
Break 1 [2]> (load "helloworld.lisp")
;; Loading file helloworld.lisp ...
;; Loaded file helloworld.lisp
#P"/Users/ex10si0n/Desktop/Lisp-Works/src/helloworld.lisp 
Break 1 [2]> (hello-world)
Hello, world
NIL
Break 1 [2]>
```
