"""
Authors:
    Katherine Butt
    Ava Reese
This is the only method for this program
It take a sentence from a file written in english and return the sentence translated into te reo māori
The key functions of this method is to seperated the different aspects of the sentence to ensure they are translated correctly
"""
def translater(userinput):
    #Verbs dictionary contains all the valid verbs that can be used in the english sentence
    #It contains all the past, present, and future versions of the valid words
    verbs = {'go':'haere', 'went':'haere','make':'hanga', 'see':'kite', 'want' : 'hiahia', 'call':'karanga', 'ask': 'pātai', 'read':'pānui','learn':'ako',
        'gone':'haere', 'made':'hanga', 'seen':'kite', 'saw':'kite', 'wanted':'hiahia', 'called':'karanga', 'asked':'pātai','learned':'ako',
        'going':'haere', 'making':'hanga', 'seeing':'kite', 'wanting':'hiahia', 'calling':'karanga', 'asking':'pātai', 'reading':'pānui', 'learning' : 'ako'}
    #Starters is an array which contains the three possible starting words in te reo, one for each tense
    starters = ['I','Kei te', 'Ka']
    #Subject dictionary contains the te reo equivalents for each type of sentence subject
    #For subjects which can occur in more than one situation keywords are used to tell between them
    subject = {'I':'au', 'We':'ahau', '(1incl)':'koe', '(1nei)':'ia', 'He':'ia', 'She':'ia','her':'ia', 'him':'ia',
    '(1excl)':'tāua','(2excl)':'māua', 'You two':'kōura', '(2incl)':'kōrua', '(2nei)':'rāua',
    '(4incl)':'tātou','(3excl)':'mātou','You':'koutou', '(3nei)':'rātou','(3incl)': 'koutou'}

    output = ""
    inputsplit = userinput.split()

    #This is a bounds checking condition which makes sure a sentence was given
    if(len(inputsplit) == 1):
        return("Error: Please use a sentence not a single word")

    lastword = inputsplit[-1]
    lastwords = inputsplit[-2] + " " + inputsplit[-1]

    #This checks to see if the subject used in the english sentence is a key word identifier
    subjectword = inputsplit[1]
    if(subjectword[0] == '('):
        subjectword += inputsplit[2]
    else:
        subjectword = inputsplit[0]

    val = '0'

    if(subjectword[0] == '('):
        val = subjectword[1]
        if(subjectword[2].isdigit()):
            val = subjectword[1] + subjectword[2]


    #Takes the last letter of the last word to determine what tense to use
    if(inputsplit[1] == "will"):
        output += starters[2] + " "
    elif(lastword[-1] == "d" or lastword[-1] == "t" or lastword == "made" or lastword == "saw"):
        output += starters[0] + " "
    elif(lastword[-1] == "g"):
        output += starters[1] + " "
    elif(len(inputsplit) >= 3 and inputsplit[2] == "will"):
        output += starters[2]
    else:
        output += starters[2] + " "

    #Translates english verbs to te reo
    if(lastword in verbs):
        output += verbs[lastword] + " "
    else:
        return("Unknown verb: " + lastwords)
    
    firstword = inputsplit[0]
    if(int(val) < 2):
        if(subjectword in subject):
            output += subject[subjectword]
    elif(int(val) == 2):
        if(inputsplit[0] == "We" or inputsplit[0] == "Us"):
            if(inputsplit[1][1] == 'i'):
                output += 'tāua'
        else:
            if(subjectword in subject):
                output += subject[subjectword]
    elif(int(val) >= 3):
        if(inputsplit[0] == "We" or inputsplit[0] == "Us"):
            if(inputsplit[1][1] == 'i'):
                output += 'tātou'
            else:
                output += 'mātou'
        elif(inputsplit[0] == "You"):
            output += 'koutou'
        elif(inputsplit[0] == 'They' or inputsplit[0] == 'Them'):
            output += 'rātou'
    else:
        return('Invalid Sentence')
    
    """
    #Translates english subject to te reo
    if(subjectword in subject):
        output += subject[subjectword]
    #This section of if else statements check for when  4 more is given
    #Determines if the subject needs to be inclusive or exclusive
    elif(int(val) >= 4):
        if(inputsplit[0] == "We" or inputsplit[0] == "Us"):
            if(inputsplit[1][1] == 'i'):
                output += 'tātou'
            else:
                output += 'mātou'
        elif(inputsplit[0] == "You"):
            output += 'koutou'
        elif(inputsplit[0] == 'They' or inputsplit[0] == 'Them'):
            output += 'rātou'
    else:
        return('Invalid Sentence')
    """
    #Need to add in a statement that only gives the output if all elements were able to be translated
    return(output)
    

if __name__ == "__main__":
    sentences = open('test.txt', 'r')
    for line in sentences:
        print(translater(line))
    

