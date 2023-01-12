# braces.py
## check if string contains braces
## if does, get the contents in between braces

import calLogic as logic

string = "((1+1)*5)/2*(25/2)"

print(string)

#string.find - find index of the first occurence of character
#string.count - count occurences of character in string

start_braces = string.count('(')
end_braces = string.count(')')

if(start_braces != end_braces):
    print("Unmatched braces!")
    exit()

# now lets get the content between the braces

start_brace = string.find('(')
end_brace = string.find(')')

contents = string[start_brace+1:end_brace]

# print(contents)

# iterate string and find all open and close braces

open_braces = []
close_braces = []

for index, letter in enumerate(string):
    if letter == '(':
        open_braces.append(index)
    if letter == ')':
        close_braces.append(index)

print(open_braces)
print(close_braces)

# check distances between indexes

for i in range(6):
    for index in range(len(open_braces)-1):
        distance1 = close_braces[index] - open_braces[index]
        distance2 = close_braces[index] - open_braces[index+1]
        print("\nIndex ", index)
        print("Comparing: ", distance1, " ", distance2)
        if( distance2 < distance1 and distance2 > 0 ):
            print("Switching")
            store = open_braces[index] # store current idx
            open_braces[index] = open_braces[index+1] #
            open_braces[index+1] = store

print("Fixed status:")
print(open_braces)
print(close_braces)
print("\n")

# print the contents between the braces

brace_index = 0

for index in range(len(open_braces)):
    contents = string[open_braces[index]+1:close_braces[index]].replace("(","").replace(")","")
    solved_contents = logic.interpret(contents,0)
    string = string.replace(contents,str(solved_contents))

print(string.replace("(","").replace(")",""))
print(logic.interpret(string.replace("(","").replace(")",""),0))
