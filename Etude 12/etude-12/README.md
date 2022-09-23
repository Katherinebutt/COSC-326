COSC326 Etude 12 Floating Point

Authors:
    Ava Reese - 2678742
    Katherine Butt - 4347525
    Matt Dixon - 5305245
    Francesca Totty - 6845575


Program Aim:
    This program takes input from a file which contains either single precision floating point values or double precision floating point values.
    The program then converts the input into IEEE equivalent and outputs to a new file

Testing Strategy:
    To test this program we used the IBM testfile provided on blackboard to test our program against to ensure it is working an producing an outcome.
    To help fix errors and bugs within the code we used the VS Code debugger which helps us to fix errors we were having such as string index out of range which occured when we were trying to extract certain aspects of a value.

Resources Used:
    To help us develop this program we used the files provided on blackboard to help undertstand what we needed to do and test our program against.
    We also used websites such as the wikipedia page: https://en.wikipedia.org/wiki/IBM_hexadecimal_floating-point#Example. This webpage gives example of the possible input types and indicates what each section of the number relates too. We found this helpful to work out were we needed to section the input to produce the correct output.
    Besides from wikipedia we also used online tutorial coding websites such as https://www.programiz.com/python-programming/file-operation. These website found using google helped us to work out how to open adn write to .bin(binary) files and other small issues we had such as working out how to covnert values to binary.
    For this program we also use the struct module. We used this module because it is useful to help convert general python strings into bytes which we needed to write into the binary file.
    We also implemented the math module which allowed us to use math.inf which produces an infinite floating point value. 

Running The Program:
    To run this program you must have a file containing either single or double precision values and a file to output the results too. Both of these files must have the .bin extension. When asked for the input seperated each component with a space and use a single character of either 's' or 'd' as the final input parameter to indicate if the input file has single or double precision values. All these files need to be in the same directory as the floating.py file.
    You may also need to make sure you have the math and struct modules installed. 