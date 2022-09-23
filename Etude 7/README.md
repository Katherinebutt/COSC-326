COSC326 Etude 7 Where In the World is CS

Author: Katherine Butt - 4347525

Program Aim:
The aim of this program is to take given geolocation in multiple formats. These formats must then be converted into a format that can be applied to a .json file which follows the correct formatting for a geojson file. This allows for the given inputs to be plotted on a map.

Testing Strategy:
For this program I used two key stategies.
    - Test file
    - Debugger
    -Test.json file
    I used a test file so that I could have more than one input tested each time the program runs. This meant that I could test for all the different input formats and ensure they are all working at the same time.
    The debugger meant that I could narrow down when something unexpected was occuring as many of the issues I had were to do with how values were being stored in variables and it being different to what I expected. I was also helpful to see why a particular format type wasn't working when others where as it would allow me to compare and contrast how they where being processed different helping me to determine what changes needed to be made.
    The test.json file allowed me to see what the output was and if it was being formated as expected. This also allowed me to apply the outputs to an online geojson map.

Resources Used:
    To help develop this program I have used the geojson.io webpage which allows .json files to be tested and applied to the map when correct. This was a key tool in ensuring the conversions between input formats was occuring correctly and that the method I developed to format the .json file was correct.
    To help develop the .json file format I used the GeoJSON Specification given in the etude document.
    Besides from these given resources a lot of googling for specifc things occured which meant I accessed many websites such as w3schools, stackoverflow and geeksforgeeks.

Running the Program:
    To run the program it requires a .txt file which contains all the geolocations to be tested. This file must be in the same directory as the program file to work. It also required for a empty file called test.json to be made and saved in the same directory as the program. Once this is done then you can run the program using the terminal in vscode. The output should appear in the test.json file unless the input is not valid in which case an invalid message should be printed to the terminal screen.

