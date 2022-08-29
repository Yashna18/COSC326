ETUDE 3 - KOCH SNOWFLAKE
Yashna Shetty - sheya140 (2901410)

The following program is a python program (running Python 3.10.4 interpretor) and can be run with the command line, or within
the terminal in VSCode.

This program uses the python standard library from python 3.10 and imports the following modules:
- turtle (to draw the koch snowflake)
- tkinter (to create the GUI)

kochsnowflake.py is a program that takes user input from the Entry widget of tkinter and uses this as the degree for the snowflake.
If the program is given anything besides a whole int, it does not build the graphical window/turtle does not start. 

Images do not dynamically resize with the window but should the user wish, they may resize the window and click "Build" again to draw a snowflake
that is approporiately sized for the current window. 

I attempted to dynamically resize the image drawn by turtle but because images are not instantaneous in turtle, even if they are hidden from the
UI, there are moments during runtime where the image is not visible as it needs to be redrawn to the resized window. 