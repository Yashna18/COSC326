import calendar
from calendar import monthrange
import re
import os

# This program takes an input file or a line from user and validates the dates by checking the following:
# 1- Whether the date is between the years 1753 and 3000 inclusive
# 2- The formatting of the dates are correct
# 3- And whether the dates are real and correct.

def main():
    print("Welcome :) This program takes a date from a file or from user_input\nand returns whether the format is valid!\n")
    info_source = input("Would you like the date to be checked from a manual entry(m), a file(f), or would you like to exit(q): ")
    start_up = 1
    while (start_up):
        if (info_source == "q"):
            start_up = 0
            break;
        elif (info_source == "m"):
            print("Enter the date to check, or exit(q): ")
            while (start_up):
                user_date = input()
                if (user_date == "q"):
                    start_up = 0
                    break;
                print(validateDate(user_date))
                print("Would you like to try another date(y) or exit(q)? ")
                user_input = input()
                if (user_input == "y"):
                    main()
                elif (user_input == "q"):
                    start_up = 0
                    break;
                break;
            break;
        elif (info_source == "f"):
            filename = input("Please enter the name of the file as filename.txt, or exit(q): ")
            while ((not (os.path.isfile(filename))) and filename != "q"):
                filename = input("\nThis is an invalid file, please try again: ")
            if (filename == "q"):
                start_up = 0
                break;
            file_dates = open(filename, 'r')
            for line in file_dates:
                print(validateDate(line))
            print("Exit? y/n")
            user_quit = input()
            if (user_quit == "y"):
                start_up = 0
                break;
            elif (user_quit == "n"):
                main()
            else:
                user_quit = input("Invalid input. Try again: ")
            break;
        else:
            info_source = input("This is not a valid option.\nPlease try again from the following options:\nManual Entry: m\nFile: f\n Quit: q\n")

# function to validate the date based off of the other functions 
# passed to the main function
# returns "Invalid" if the any of the month, year, or date functions return "Invalid"

def validateDate(entered_date):
    list_of_months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    date = entered_date.strip()
    try:
        first_sep = re.search("[-/\s\n]", date).group()
        print(first_sep)
    except AttributeError:
        first_sep = re.search("[-/\s\n]", entered_date)
    try:
        final_date = re.split(first_sep, date)
    except TypeError:
        final_date = date.split('\n')
    print(final_date)
    if (len(final_date) != 3):
        return "Invalid seperators!\n"
    checked_year = checkYear(final_date[2])
    checked_month = checkMonth(final_date[1], list_of_months)
    if (checked_year != "Invalid"):
        if (checked_month != "Invalid"):
            if (type(checked_month) is str):
                month_num = list_of_months.index(checked_month)
            else:
                month_num = checked_month
            checked_day = checkDay(final_date[0], month_num, checked_year)
            if(checked_day != "Invalid"):
                return "This is a valid date\n"
            else:
                return "Incorrect day!\n"
        else:
            return "Incorrect month!\n"
    else:
        return "Incorrect year!\n"

# function to validate the year given by the user or file
# returns "Invalid" if the year is outside the range of 1753-3000 inclusive
def checkYear(date_z):
    length_year = len(date_z)
    if (length_year != 2):
        if (length_year != 4):
            return "Invalid"
    try:
        year = int(date_z)
    except ValueError:
        return "Invalid"

    if (length_year == 4):
        if (year < 1753):
            return "Invalid"
        elif (year > 3000):
            return "Invalid"
    elif (length_year == 2):
        if (year <= 99 & year >= 50):
            year += 1900
        else:
            year += 2000
    return year

# function to validate the month given by the user or file
# returns "Invalid" if the month is not given within a specified format
# or not a real month

def checkMonth(date_y, valid_months):
    length_month = len(date_y)
    try:
        month = int(date_y)
    except ValueError:
        try:
            month = str(date_y)
        except ValueError:
            return "Invalid"
    if (type(month) is int):
        if (month < 1 | month > 12 | length_month > 2):
            return "Invalid"
        else:
            return month
    else:
        if (month in valid_months):
            return month.capitalize()
        elif (month in (x.lower() for x in valid_months) or month in (x.upper() for x in valid_months)):
            return month.capitalize()
        else:
            return "Invalid"

# function to validate the day based on the checked month and checked year.
# returns "Invalid" if the date is outside the range of the given month and
# year.

def checkDay(date_x, checked_month, checked_year):
    length_day = len(date_x)
    if (length_day != 2):
        if (length_day != 1):
            return "Invalid"
    try:
        day = int(date_x)
    except ValueError:
        return "Invalid"
    try:
        num_days = monthrange(checked_year, checked_month)[1]
        if (day <= 0 | day > num_days ):
            return "Invalid"
    except calendar.IllegalMonthError:
        return "Invalid"
    return day


if __name__ == "__main__":
    main()
