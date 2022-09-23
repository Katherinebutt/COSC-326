"""
COSC326 Etude 7
Where in the World is CS
Author: Katherine Butt
Date: May 2022
"""

"""
This is the main function for the program
It takes the users inputs
Checks and validates the users input using a series of
if else statements
This function also checks for single valued inputs.
"""
def chooser(userinput):
    #This checks for when a text only input is given
    if(userinput[0].isalpha()):
        return("Invalid Input")
    unchangedinput = userinput
    inputsrmv = str(userinput.replace(',',''))
    inputsrmv = inputsrmv.replace('"',"''")
    #Checks to determine if the input is of DMS input
    if(('°' in inputsrmv and "'" in inputsrmv) or ('d' in inputsrmv and 'm' in inputsrmv)):
        return(dmsconverter(inputsrmv, unchangedinput))
    else:
        inputsrmv = inputsrmv.replace('+','')
        inputsrmv = inputsrmv.replace('°','')
        inputsrmv = inputsrmv.strip('\n')
        inputs = inputsrmv.split(" ")
        name = ''
        temp = inputsrmv.split(".")
        if(inputs[-1].isalpha() and len(inputs[-1]) > 1):
            name = '"name" : "' + inputs[-1] + '"'
            inputs = inputs[:-1]
        if(len(inputs) == 4):
            inputs = (inputs[0] + inputs[1]) , (inputs[2] + inputs[3])
        """
        This if statement checks for inputs where only the values before the decimal are given
        It gives the user benefit of the doubt and assumes they are valid.
        For consistent formating it gives 6 decimal places to the input
        """
        if(len(temp)==1 and len(inputs) ==2):
            lon = inputs[0] + "." + '000000'
            lat = inputs[1] + "." + '000000'
            finalvals = (lat + " " + lon)
            return(writer(finalvals, name))
        return(sfchecker(inputs,name, unchangedinput))
    
"""
This function is for inputs which follow the Degrees, Minutes, Second format
It uses a series of replace statements which produces a standard format
Based off the possible different lengths of the input the dms values can occur
the d, m and,s sectioning is different hence the if else statements which check the length
A mathmatical formula is then applied to convert the DMS format to standard form.
Once in standard for the SFchecker function is returned
"""
def dmsconverter(inputs, unchangedinput):
    """
    These replace statements help to generate a consistent
    format which can then be used to generate the final form
    """
    ns = ''
    ew = ''
    name = ''

    dmsvals = inputs.replace(" ","")
    dmsvals = dmsvals.strip('\n')
    dmsvals = dmsvals.replace('d'," ")
    dmsvals = dmsvals.replace('s',' ')
    dmsvals = dmsvals.replace('m',' ')
    dmsvals = dmsvals.replace("°",' ')
    dmsvals = dmsvals.replace('"', ' ')
    dmsvals = dmsvals.replace("''",' ')
    dmsvals = dmsvals.replace("'", " ")
    dmsvals = dmsvals.replace(".", ' ')
    dmsvals = dmsvals.replace(",", " ")
    dmsvals = dmsvals.split(" ")

    d1 = float(dmsvals[0])
    m1 = dmsvals[1]
    s1 = dmsvals[2]

    if(len(dmsvals) >= 8):
        if not(dmsvals[7].isalpha()):
            s1 = s1+dmsvals[3]
            d2 = dmsvals[4]
            m2 = dmsvals[5]
            s2 = dmsvals[6] + dmsvals[7]
    elif(dmsvals[6].isalpha()):
        d2 = dmsvals[3]
        m2 = dmsvals[4]
        s2 = dmsvals[5]
    else:
        d2 = dmsvals[4]
        m2 = dmsvals[5]
        s2 = dmsvals[6]

    if(d2[0].isalpha()):
        ns = d2[0]
        d2 = d2[1:]

    if(len(dmsvals) == 8):
        ew = dmsvals[7]
    if(len(dmsvals) == 9):
        if(dmsvals[8][0] == 'E' or dmsvals[8][0] == 'W'):
            ew = dmsvals[8][0]
        if(len(dmsvals[8]) > 1):
            if(dmsvals[8][1].isalpha()):
                name = '"name" : "' + dmsvals[8][1:] + '"'

    d2 = float(d2)

    lat = d1 + float(m1)/60 + float(s1)/60000
    lon = d2 + float(m2)/60 + float(s2)/35000
    forlat = "{:.6f}".format(lat)
    forlon = "{:.6f}".format(lon)

    """
    Probably not the best way to do this check
    """
    if(ns == 'S'):
        forlat = str(-abs(float(forlat)))
    if(ew == "W"):
        forlon = str(-abs(float(forlon)))
    vals = forlat, forlon
    return(sfchecker(vals, name, unchangedinput))
    
"""
This method is responsible for ensuring the input is within allowable ranges
It also uses the zeroschecker method which ensures that the final format for all inputs
has 6 decimal places
It checks for the hemisphere of the input by checking for 'NSEW+-' characters
"""
def sfchecker(userinput, name, unchangedinput):
    #Need to add in a check for whether something is standard form or another input format
    northhem = False
    east = False
    vals = userinput
    #Checking for standard form
    #Accounts for when a comma is used to seperate the input
    #Also works when no comma is used
    
    try:
        if(vals[0][-1] == ','):
            lat = vals[0][:-2]
            lon = vals[1]
        else:
            lat = vals[0]
            lon = vals[1]
    except:
        print("Unable to process: " + unchangedinput)
        return
    #Checking for north or south hemisphere
    #Checking for either a negative symbol or for NSEW notations
    if(lat[-1].isalpha() or lon[-1].isalpha()):
        if(lat[-1] == 'S'):
            northhem = False
            lat = lat[:-1]
        elif(lat[-1] == 'N'):
            northhem = True
            lat = lat[:-1]
        #Check for if the lat and long are given in the wrong order
        elif(lat[-1] == 'W' or lat[-1] == 'E'):
            temp = lon[:-1]
            lon = lat[:-1]
            lat = temp
        #Checking for east or west hemispheres
        if(lon[-1] == 'W'):
            east = False
            lon = lon[:-1]
        elif(lon[-1] == 'E'):
            east = True
            lon = lon[:-1]
        #Check for if the lat and lon are given in the wrong order
        elif(lon[-1] == 'S' or lon[-1] == 'N'):
            temp = lat[:-1]
            lat = lon[:-1]
            lon = temp
    else:
        if(lat[0].isdigit()):
            northhem = True
        if(lon[0].isdigit()):
            east = True
        if(lat[0] == '-'):
            lat = lat[1:]
        if(lon[0] == '-'):
            lon = lon[1:]

    #Need to assigned what is returned from here so it is correct for the rest of the method
    returnedvals = zeroschecker(lat, lon)
    lat = returnedvals[0]
    lon = returnedvals[1]
    #Need to make sure that the values given for standard form are within the valid ranges
    latsplit = lat.split('.')
    lonsplit = lon.split('.')
    twolat = latsplit[0]
    threelon = lonsplit[0]
    if not (int(twolat) > -90 or int(twolat) < 90):
        print("Unable to process: " + userinput[0] + userinput[1] + name)
        return
    elif not(int(threelon) > -180 or int(threelon) < 180):
        print("Unable to process: " + userinput[0] + userinput[1] + name)
        return()
    else:
        #This section formats the output after the checks for standard form
        if(northhem == False):
            if(east == False):
                finalvals = ("-"+ lat + " " + "-" + lon)
            else:
                finalvals = ("-" + lat + " " + lon)
        elif(northhem == True & east == False):
            finalvals = (lat + " " + "-" + lon)
        else:
            finalvals = (lat + " " + lon)
    return(writer(finalvals, name))

def zeroschecker(lat, lon):
    #Checking for 6 zeros after point
    lataddzeros = 0
    lonaddzeros = 0
    latsplit = str(lat).split('.')
    lonsplit = str(lon).split('.')
    if((len(latsplit[1]) != 6) & (len(lonsplit[1]) != 6)):
        lataddzeros = 6 - len(latsplit[1])
        lonaddzeros = 6 - len(lonsplit[1]) 
    #Making sure there is 6 zeros after the decimal point
    while(lataddzeros > 0):
        lat += '0'
        lataddzeros -= 1  
    while(lonaddzeros > 0):
        lon += '0'  
        lonaddzeros -= 1
    return(lat, lon)

"""
This function allows for the users input to be added to a file
This file is then given to a geomapping website
File type required is .json
File must be formated correctly to work
"""
def writer(value, name):
    splval = value.split()
    file = open("test.json", 'a')
    #Need to format the value into the form required to put onto the map
    file.write('\n      {\n     "type": "Feature",\n        "properties":{ ')
    file.write(name)
    file.write('},\n        "geometry": {\n          "type": "Point",\n          "coordinates": [\n            ')
    file.write(splval[1])
    file.write(',\n            ')
    file.write(splval[0])
    file.write('\n       ]\n      }\n     },\n')
    file.close()

""" 
This function ensure the json file is formatted correctly
at the end so that it can be run by geojson.io
"""
def filefinisher():
    file = open("test.json",'r')
    lines = file.readlines()
    lines[-1] = ('    }\n')
    file.close()
    file = open("test.json",'w')
    file.writelines(lines)
    file.write('  ]\n}')
    file.close()
"""
This function occurs once.
It occurs when the program begins running and preps the json file
for inputs
"""
def filestarter():
    file = open("test.json", 'w')
    file.write('{\n   "type": "FeatureCollection",\n  "features": [')
    file.close

if __name__=="__main__":
    values = open("values.txt", 'r')
    filestarter()
    for line in values:
        userinput = line
        (chooser(userinput))
    filefinisher()