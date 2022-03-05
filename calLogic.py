#imports
import math
import trig
#####   INTERPRET
#vars
operators = ["+","-","*",'/']
#def
def interpret(args,ans):
    temp_storage = ['']*32
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
    #Strip empty space
    temp_storage[:] = (value for value in temp_storage if value != '')
    #parse all exceptions: exponent, sqrt, logarithms and trig functions
    index = 0
    for element in temp_storage:
        factor = 1
        if("√" in element): #parse sqrt
            sqrt_index = element.index("√")
            if(sqrt_index!=0): #check factor before sqrt
                factor=float(element[:sqrt_index])
            temp_storage[index] = factor * math.sqrt(float(element[(sqrt_index+1):]))
        elif("-" in element and index == 0): #check if first element is negative
            temp_storage[index+1] = float(temp_storage[index+1])*-1
            temp_storage.pop(index)
        elif("^" in element): #parse exponent
            exp_index = element.index("^")
            base = float(element[:exp_index])
            exp = float(element[(exp_index+1):])
            temp_storage[index] = math.pow(base,exp)
        elif("log" in element): #parse logarithms
            log_index = element.index("log")
            if(log_index != 0):
                factor = float(element[:log_index])
            temp_storage[index] = factor * math.log10(float(element[(log_index+3):]))
        elif("sin" in element): #parse trig functions
            sin_index = element.index("sin")
            value = float(element[(sin_index+3):])
            if(sin_index != 0):
                factor = float(element[:sin_index])
            temp_storage[index] = factor * trig.sin(value)
        elif("cos" in element):
            cos_index = element.index("cos")
            value = float(element[(cos_index+3):])
            if(cos_index != 0):
                factor = float(element[:cos_index])
            temp_storage[index] = factor * trig.cos(value)
        elif("tan" in element):
            tan_index = element.index("tan")
            value = float(element[(tan_index+3):])
            if(tan_index != 0):
                factor = float(element[:tan_index])
            if(trig.tan(value) == "undefined"):
                return "undefined"
            temp_storage[index] = factor * trig.tan(value)
        elif("cot" in element):
            cot_index = element.index("cot")
            value = float(element[(cot_index+3):])
            if(cot_index != 0):
                factor = float(element[:cot_index])
            if(trig.cot(value) == "undefined"):
                return "undefined"
            temp_storage[index] = factor * trig.cot(value)
        elif("ans" in element):
            ans_index = element.index("ans")
            if(ans_index != 0):
                factor = float(element[:ans_index])
            temp_storage[index] = factor * float(ans)
        index = index + 1
    #return solved expression to JS
    return solve(temp_storage,ans)

#####   SOLVE
def solve(temp_storage,ans):
    #first solve multiplication and division
    index = 0
    for element in temp_storage:
        if(temp_storage[index]=='*' or temp_storage[index]=='/'):
            if(temp_storage[index]=='*'):
                temp_storage[index-1]=float(temp_storage[index-1])*float(temp_storage[index+1])
            else:
                temp_storage[index-1]=float(temp_storage[index-1])/float(temp_storage[index+1])
            temp_storage.pop(index)
            temp_storage.pop(index)
            continue
        index = index + 1
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
def log(args):
    try:
        for element in args:
            print(">",element, end =" ")
        print("")
    except:
        print("> invalid args passed to log()")
