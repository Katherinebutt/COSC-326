import turtle
import tkinter as tk
from tkinter import ttk

"""
Koch Snowflake Program
Author: Katherine Butt

This program uses a recursive algorithm to draw a koch snowflake
The user is able to use a slider and button to control the number of times the recursion occurs
Depending on how many times the recursion occurs different orders of the snowflake building process are drawn
"""

"""
The main purpose of this function is the recursion required to to produce the snowflake
This function is called from the drawSnowflake function once the user input has been gained
This function runs for as many order given by the user
"""
def snowflake(sidelength, i):
    if i == 0:
        t.forward(sidelength)
        return
    sidelength /= 3.0
    snowflake(sidelength, i-1)
    t.left(60)
    snowflake(sidelength, i-1)
    t.right(120)
    snowflake(sidelength, i-1)
    t.left(60)
    snowflake(sidelength, i-1)

"""
This function is responsible for getting the user input and initating the snowflake drawing
This function holds all the commands to get the turtle element of the program to begin running
"""
def drawsnowflake():
    order = (inputval.get()-1)
    size = root.winfo_width()-200
    
    t.penup()
    t.backward(size/2.0) #This makes sure that the snowflake is centered
    t.pendown()

    for i in range(3):
        snowflake(size, order) #Calls to the recursive function
        t.right(120)

"""
The following code produces the gui window and allows for the tkinter and turtle modules to be on the same window
It sets all the defaults required fro the gui window and the interation that allow it to be resizeable
"""
root = tk.Tk()
root.geometry("500x500")    #This sets the base size of the window
root.minsize(250,250)
root.resizable(True,True) #This allows the window to be resizeable by both the width and the height
canvas = tk.Canvas(master = root) #Adding the canvas to the root window
canvas.pack(expand=True, anchor="center") #Allowing the canvas to be expanded and centering

"""
This section of code adds all the elements required to the gui window
This means that all element are shown to the user
"""
t = turtle.RawTurtle(canvas)
inputval = tk.DoubleVar()
s = tk.Scale(master = root, label='Pick your order', from_=1, to=10, orient=tk.HORIZONTAL,
 length=200, showvalue=0,tickinterval=1, variable=inputval, command=drawsnowflake).pack(side=tk.LEFT, anchor="sw")
tk.Button(master = root, text = "Next", command = drawsnowflake).pack(side=tk.LEFT, anchor="sw")

"""
This section of code generated the sizegrip which allows the window the be resized
"""
sizing = ttk.Sizegrip(root)
sizing.pack(side="right", anchor="se")

root.mainloop()