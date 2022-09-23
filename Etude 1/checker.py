import re
"""
Date Checking and Validation Program
Author: Katherine Butt

This is the key method of the program, it is used to check the date inputted
The argument given in the method is the date that the user inputs
The first part of the method checks if the input is valid and therefore worthwhile checking
"""
def checker(dateinput):
    dateinput = dateinput.strip('\n')
    date = re.split(r'-|\s|/', dateinput)
    seps = re.sub(r'[^-|\s|/]', '', dateinput)
    
    #Checking to make sure the correct number of seperators and values have been inputted
    if(len(seps) !=2):
        return '{} - Input is invalid, {} separators were found, {}'.format(dateinput, len(seps), "You can only use 2 seperators. Acceptable seperators are: '/','-', or <space>.")
    if not(len(date)==3):
        return '{} - Input is invalid, {}'.format(dateinput, "You must input 3 values seperated using 2 seperators. Acceptable seperators are: '/','-', or <space>.")
    
    #Checking to make sure that only seperator is used per input
    errors = []
    if(len(set(seps))!=1):
        errors.append("must use same seperator for the entire input")
        
    #Setting the 3 sections of the input to there own variables
    day = date[0]
    month = date[1]
    year = date[2]
    
    """
    The following code checks the date
    It uses defined methods futher in the program to check different aspect of the date input
    """
    try:
        month = month_format(month)
        try:
            year = year_format(year)
            if(year < 1753) or (year > 3000):
                year = 'error'
                errors.append("year entered is out of valid range. Valid range is from 1753 t0 3000")
        except ValueError:
            year = 'error'
            errors.append("Year entered is invalid")
    except ValueError:
        month = 'error'
        errors.append("Month entered is invalid")

    if((month == 'error') | (year == 'error')):
        errors.append("Unable to verify the day due to either an invalid month or year")
    elif(day.isdigit):
        if(len(day) >2):
            day = 'error'
            errors.append("Date entered is invalid. Can only be a maximum of two numbers")
        elif(day == '0' or day == '00'):
            day = 'error'
            errors.append("Day value must be greater than 0")
        else:
            day1 = day_leap_year(int(day),month,year)
            day = str(day1).zfill(2)
    elif((day == 'error') | (month == 'error') | (year =='error')):
        errors.append("Unable to verify date due to invalid input")

    if(len(errors) >= 1):
        return '{} - INVALID: {}'.format(dateinput, ", ".join(errors) + ".")
    else:
        return '{} {} {}'.format(day,month,year)

"""
This method is used to check the day aspect of the input
It also makes sure the day is within the bounds of the month length
This is achieved using a dictionary to assign lengths to months
Also has a system to check for a leap year which changes the allowable dates for feb     
Arguements takes are the day, month, and year variables which are generated from splitting the date inputted 
""" 
def day_leap_year(day, month, year):
    month_lengths = {'Jan':31,'Feb':28,'Mar':31,'Apr':30,'May':31,'Jun':30,'Jul':31,'Aug':31,'Sep':30,'Oct':31,'Nov':30,'Dec':31}    
    if((year % 4 == 0) & (year % 100 != 0) or (year == 00) or (year == 2000)):
        month_lengths['Feb'] = 29
    if(day > 0):
        if((day <= (month_lengths[month])) & (day > 0)):
            return day
        else:
            return 'INVALID: The value entered for the day is not valid for: '

"""
This method is used to check the month aspect of the input is correct
To convert between a digit month repersentation and a string repersentation
The list of months is used to convert a digit by extracting the month stored in the index position of the digit
Argument taken is the month variable which is taken from splitting the date inputted
"""
def month_format(month):
    all_months = ['Jan','Feb','Mar','Apr','May','Jun',
              'Jul','Aug','Sep','Oct','Nov','Dec']
    if(month.isdigit()):
        if(len(month) > 2):
            raise ValueError #Section of input is not valid
        else:
            month = int(month)
            if((month > 0) & (month <= 12)): #Making sure date entered is within bounds
                return all_months[month-1]
            else:
                raise ValueError
    elif(month.capitalize() in all_months):
        return month.capitalize()
    else:
        raise ValueError
"""
This method is used to check the year asepct of the input
It checks the year using bounds checking by implementing if/else statements
It also contains the rules for if only 2 digits are given for a year
Argument taken is the year variable which is take from spliting the date inputted 
"""           
def year_format(year):
    if(year.isdigit()):
        if((len(year) != 4) & (len(year) != 2)):
            raise ValueError
        if((len(year) == 4) & (year[0] == '0')):
            raise ValueError
    else:
        raise ValueError
        
    year = int(year)    
    if(year <= 99):
        if(year >= 50):
            year += 1900
            return year
        else:
            year += 2000
            return year
    else:
        return year

if __name__ == '__main__':
    #This is used to run the checker method and produce an output to the user based on their input
    while(True):
        date = str(input("Please enter a date to check or f to finish:\n"))
        if(date == "f"):
            break
        else:
            print(checker(date))