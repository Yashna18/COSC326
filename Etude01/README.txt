Yashna Shetty - 2901410 (sheya140)

The test cases used for this program is in dates.txt - sent with this README and dates.py file.

This program is used to validate both the format and the correctness of any given date.

A single date must have consistent use of seperators and must follow the following formatting:
	--> day: dd or d or 0d
	--> month: mm or m or 0m or the first three letters of the month name (all in the same case, or
	 	   with the first letter in upper-case).
	--> year: between the years of 1753 and 3000
		  yy or yyyy
	--> seperators: - or / or <space>

This program takes in a date and seperates the date into 3 components (based on the specified seperators). 
If it is unable to seperate the given date into three parts, returns either the day, month, or year as 
invalid, or finds inconsistent use of the seperators, it returns "Invalid" to the user and specifies what
the incorrect action within the given date was. 

This is a python 3.10 file that can be run with the command line, or within a terminal in VSCode. 
Should the test cases from the input file be used, either the path to the filename.txt or (if the filename.txt is 
in the same folder) the filename.txt should be specified. 
