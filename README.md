chomp
=====

Implementation of chomp game exercise.
Part of OSBridge 2013.  

http://opensourcebridge.org/wiki/2013/Shall_We_Play_A_Game%3F

## Some notes:

Moves are specified in the form: `x,y` and are zero-based.

(and this differs from Bart's solution)

You can specify an arbitrary board size on the commandline:

`./chomp.py 8 3` for example

## What's good:

I like that my Board is an immutable object.

## What's bad:

* The negamax result tuple feels klunky.
* There are lost of cleanups to be done.
* I'm probably not Pythonic enough.  I wish I was.

## Odd strangeness:

A board 8x4 with an initial human move of 3,3 seems to not return.  Recursion loop from hell?
