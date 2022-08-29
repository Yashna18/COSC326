Etude 11 - Video Manager
@author - Yashna Shetty
@author - Jakub Sawicki 

The following program is a singleton implementation of a VideoManager class
which takes in a video clip and adds or deletes it to the dictionary. 

To run this program (in VSCode):
Please follow these instructions.
Note: you will be needing NET6.0 instead of the mentioned 5.0 from the
article below. 
https://travis.media/how-to-run-csharp-in-vscode/

A possible issue we see with the VideoManager is the potential for it to
cause issues in writing testable code. This is a common issue with programs
that use singleton design patterns. That is, without implementation of an
entire class, there is no way to test.