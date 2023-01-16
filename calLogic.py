##### calLogic.py
# Main calculator functionality
# Meant to be called from outside
# Point of entry is def interpret(args, ans)

#imports
import math
import braces
import convert

#####   INTERPRET
def parse_args(args):
    #default values
    operators = ["+","-","*",'/']
    temp_storage = ['']*64
    result = list(args)

    #parse all operators and slot them in individual indexes
    index = 0
    check = 0

    for element in result:
        if(element in operators) and check == 0:
            index = index + 1
            temp_storage[index] = element
            index = index + 1
            check = 1 #check to prevent 2 consecutive operators
        else:
            temp_storage[index] = temp_storage[index]+element
            check = 0
    #strip empty space
    temp_storage[:] = (value for value in temp_storage if value != '')

    #prevent first element from being an operator
    if temp_storage[0] in operators:
        if temp_storage[0] == '-':
            temp_storage[1] = '-'+temp_storage[1]
        temp_storage.pop(0)

    return temp_storage

#### INTERPRET
def interpret(args,ans=0):
    #account for number system conversions and logic operations
    temp_args = args.split(" ")
    conversion_tgts = ["BIN","OCT","HEX","DEC"]
    logic_tgts = ["AND","OR","NOT","NOR","NAND","XOR","XNOR"]

    if len(temp_args) > 3:
        if (temp_args[0].upper() in conversion_tgts) and ((temp_args[2].upper() in logic_tgts) or (temp_args[3].upper() in logic_tgts)):
            #we're looking at a logic operation
            result = convert.parse_operation(temp_args)

            return result

    if len(temp_args) == 3:
        if (temp_args[0].upper() in conversion_tgts) and (temp_args[2].upper() in conversion_tgts):
            #we're looking at a direct conversion
            result = convert.parse_conversion(temp_args)

            return result

    #account for braces
    if ('(' in args):
        return braces.check_braces(args)

    #check if passed args is already a parsed array
    if isinstance(args,list):
        temp_storage = args
    else:
        temp_storage = parse_args(args)

    #parse all exceptions: exponent, sqrt and ans
    index = 0

    for element in temp_storage:
        factor = 1
        if("√" in element): #parse sqrt
            sqrt_index = element.index("√")
            if(sqrt_index!=0): #check factor before sqrt
                factor=float(element[:sqrt_index])
            temp_storage[index] = factor * math.sqrt(float(element[(sqrt_index+1):]))
        elif("^" in element): #parse exponent
            exp_index = element.index("^")
            base = float(element[:exp_index])
            exp = float(element[(exp_index+1):])
            temp_storage[index] = math.pow(base,exp)
        elif("ans" in element):
            ans_index = element.index("ans")
            if(ans_index != 0):
                factor = float(element[:ans_index])
            temp_storage[index] = factor * float(ans)
        index = index + 1

    #return solved expression to JS
    return solve(temp_storage,ans)

#####   SOLVE
def solve(temp_storage,ans=0):
    print("Called with: ", temp_storage)

    #first solve multiplication and division
    index = 0
    for element in temp_storage:
        # add modulo operation from Žiga
        if(temp_storage[index]=='*' or temp_storage[index]=='/'):
            if(temp_storage[index]=='*'):
                temp_storage[index-1]=float(temp_storage[index-1])*float(temp_storage[index+1])
            else:
                temp_storage[index-1]=float(temp_storage[index-1])/float(temp_storage[index+1])
            temp_storage.pop(index)
            temp_storage.pop(index)
            continue
        index = index + 1

    #redundant multiplication and division check
    if ('*' in temp_storage) or ('/' in temp_storage):
        val_storage = solve(temp_storage,ans)

    #now solve addition and subtraction
    val_storage = 0

    #redundant negative first element check
    if(temp_storage[0]=='-'):
        val_storage = float(temp_storage[1])*-1
        temp_storage.pop(0)
    else:
        val_storage = float(temp_storage[0])

    #now finally solve
    index = 0
    for element in temp_storage:
        if(element == '+'):
            val_storage = val_storage + float(temp_storage[index+1])
        elif(element == '-'):
            val_storage = val_storage - float(temp_storage[index+1])
        index = index + 1
    return val_storage

##### log
def debug(args):
    try:
        for element in args:
            print(">",element, end =" ")
        print("")
    except:
        print("> invalid args passed to log()")
