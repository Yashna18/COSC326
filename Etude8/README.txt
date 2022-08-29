# ETUDE 8 Rational Thinking
Yashna Shetty and Cameron Moore-Carter


For this etude, we were able to find various references online to help with the implementation of the
Integer class.
At first, we were able to grasp a general idea of the behaviour of strings after reading a tutorial
on geeksforgeeks:
https://www.geeksforgeeks.org/bigint-big-integers-in-c-with-example/
We were able to implement this to suit our own needs for the Integer class. 
Various other resources for the implementation of our code can be found in the comments of the
working code. 

For divide was tricky and we tried to do a long division implementation but it wasnt working, we were
successful with a long multiplication implementation. With that info we were able to implement a
rationals class with numerators and denominators made of Integer objects. For the Integer we used
char arrays and minused the ascii value to get what was essentially an int array but it worked for the
better with char operations and accesses.

How to run:
Run the make file and run the exe

Test Cases:
3.125/2 --> 1 9/16
7/6 --> 1 1/6
637285 * 482950
-355423 - -22236
1/4 * 2/3 = 1/6
1/2 - 2/34 = 15/34