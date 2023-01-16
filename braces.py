# braces.py
## check if string contains braces
## if does, interpret the contents in between braces

import calLogic as logic

def check_braces(string):

    start_braces = string.count('(')
    end_braces = string.count(')')

    if(start_braces != end_braces):
        print("Unmatched braces!")
        return "err"

    # iterate string and find all open and close braces

    open_braces = []
    close_braces = []

    for index, letter in enumerate(string):
        if letter == '(':
            open_braces.append(index)
        if letter == ')':
            close_braces.append(index)

    # check distances between indexes

    for i in range(len(open_braces)):
        for index in range(len(open_braces)-1):
            distance1 = close_braces[index] - open_braces[index]
            distance2 = close_braces[index] - open_braces[index+1]

            if( distance2 < distance1 and distance2 > 0 ):
                store = open_braces[index] # store current idx
                open_braces[index] = open_braces[index+1] #
                open_braces[index+1] = store

    # print the contents between the braces

    for index in range(len(open_braces)):
        contents = string[open_braces[index]+1:close_braces[index]].replace("(","").replace(")","")
        solved_contents = logic.interpret(contents,0)
        string = string.replace(contents,str(solved_contents))

    parsed_string = string.replace("(","").replace(")","")
    result = logic.interpret(parsed_string)

    return result

#

if __name__ == '__main__':
    string = "5 * ( 3 + 4 )"
    check_braces(string)
