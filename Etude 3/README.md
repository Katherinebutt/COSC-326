COSC326 Etude 3 Koch Snowflake

For this program I have imported and used three modules
    1. tkinter
        - This module is the main python module used to produce GUI interfaces. For this program I have used the build in functions that are part of the module such as Button, Scale and Canvas. These elements of the module enabled me to make the gui interface interactive and work alongside the Turtle module which I used to draw the snowflake
    2. ttk (This module can only be used with tkinter)
        - This module is used like an extension to the tkinter module. It gives access to additional widgets that work with the tkinter elements. In this program I used ttk to make the gui interface resizeable using the Sizegrip function. This I felt was the easiest way to make my gui resizeable due to already using function like pack which alongside sizegrip allow any packed elements to automatically resize/move when the gui window size is changed
    3. turtle
        - This module is used to produce gui drawings. This module also works alongside the tkinter module well as it is based of some of the same graphics. In my program the turtle module is used in my recursive method to draw the snowflake

Testing Strategy:
    To test my program I began by only drawing the snowflake when the program runs then slowing integrating the elements required to make it interactive. At each step of the intergration I would check to see if the program was still running and if any error messages were being produced.
        - Any error messages I would search for using google to determine what was causing the issue, or I would then use the debugger to see where the program was breaking which I found useful to narrow down where the error was coming from

Resources Used:
    For this etude I found youtube tutorials useful to understand how the koch snowflake worked and how to get a turtle and tkinter elements on the same gui window and not on two seperate ones. Beside from this I mainly used google to search for anything I needed too.

Running the Program:
    To run the program open snowflake.py file using visual studio
    Use the inbuilt run function of visual studio
        This should automatically open the GUI interface and move you too it
    Then use the slider down the bottom  of the GUI interface to select what order you would like to draw
    Once this has been selected press the next button and your drawing should begin
    If you wish to resize the window this can be done from clicking on the bottom right of the GUI window

Improvements:
    I have used the tracer() function so that only the fully drawn snowflake it displayed
    The error that was occuring with the slider has been fixed
    I have found a way that allows for the size of the snowflake to not be hardcoded and for the size of the snowflake to be resized when the window size changes

    2nd Resubmission:
    Updated the code so that the resizing occurs automatically
    Have also made sure the snowflake is centred
    Increased the minsize so that the button and slider don't get cut off
    Stopped drawings from occuring overtime of each other t.clear()
