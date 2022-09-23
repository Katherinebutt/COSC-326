COSC326 Etude 1 Dates

For this program I have used the RE module which allows me to use regular expressions
This made it easier to split the input from the user.
The two functions of the RE module I used are the re.split which is used to split the input into the 3 sections(day,month,year)
I also used re.subs which is used to subsitute the seperating characters used so they can be counted for bounds checking

Testing Stratgey:
    To test my program I inputted a series of valid and invalid dates once all asepcts were completed
    During the development phases I did begin by checking the program using print statements to work out where the program was reaching however towards the end I found that using a debugger was an easier way to see where the program was breaking
    Examples of test inputs are:
        12/02/98
        12/Jul/3000
        7/12/1760
        7/12/1700

Resources Used:
    To help me create this program I used a mixture of watching youtube videos, and using google to search and find solutions to any problems I was having this lead me to websites such as stackoverflow, tutorialpoint and W3Schools

Running the Progam:
    To run the program open the checker.py file using visual studio
    Use the run fuction provided by visual studio
    Then using the terminal window in visual studio code follow the prompts to enter a date
    The terminal is also where the output should be seen if the input was valid the date will be presented in the correct format if it is not valid then an Invalid notice will be given

Improvements:
    I have worked on ensuring that the program works well to avoid and deal with invalid inputs
    I have also adjusting the program to ensure it works with python 3 as well as python 2

    Another improvement made to this program was ensuring the user gets a helpful error message when the day entered is not valid for the given month

    Using the zfill function the program is able to ensure that the output is formatted correctly by making sure the day consists of 2 values