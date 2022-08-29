ETUDE 5 - LOOK WHO'S TALKING
Yashna Shetty - sheya140 (2901410)
Remin Reji Mathew - rejre960 (2581103)

The follow program is a python program (running Python 3.10.4 interpretor)
and can be run with the command line, or within the terminal in VSCode.

The program uses the python standard library from python 3.10 and imports:
- sys
- re

lookwhostalking.py takes input from the user and reads it in line by line.
it proceeds to check the formatting of the sentence and if the sentence 
passes the check, it proceeds to translate the sentence into Māori.

To use this program:
The formatting of the sentence is as follows:
[pronoun][(no.of people "excl"/"incl")][tense][verb]
- Pronouns that can only refer to more than one person will always require
  the user to specify how many people and who they are referring to.
where:

-> "incl": referring to the listener
-> "excl": not referring to the listener

writing "quit" at any point exits the program. 