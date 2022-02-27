#imports
import math
#####   INTERPRET
#vars
operators = ["+","-","*",'/']
#def
def interpret(args):
    temp_storage = ['']*32
    index = 0
    result = list(args)
    #parse all operators and slot them in individual indexes
    for element in result:
        if(element in operators):
            index = index + 1
            temp_storage[index] = element
            index = index + 1
        else:
            temp_storage[index] = temp_storage[index]+element
    #parse all exceptions: exponent, sqrt, logarithms and trig functions
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
        elif("log" in element): #parse logarithms
            log_index = element.index("log")
            if(log_index != 0):
                factor = float(element[:log_index])
            temp_storage[index] = factor * math.log10(float(element[(log_index+3):]))
        elif("sin" in element): #parse trig functions
            sin_index = element.index("sin")
            if(sin_index != 0):
                factor = float(element[:sin_index])
            if((float(element[(sin_index+3):])/90)%2==0):
                temp_storage[index] = 0
            else:
                temp_storage[index] = factor * math.sin(math.radians(float(element[(sin_index+3):])))
        elif("cos" in element):
            cos_index = element.index("cos")
            if(cos_index != 0):
                factor = float(element[:cos_index])
            if((float(element[(cos_index+3):])/90)%2!=0):
                temp_storage[index] = 0
            else:
                temp_storage[index] = factor * math.cos(math.radians(float(element[(cos_index+3):])))
        elif("tan" in element):
            tan_index = element.index("tan")
            if(tan_index != 0):
                factor = float(element[:tan_index])
            tan_value = element[(tan_index+3):]
            temp_storage[index] = factor * math.tan(math.radians(float(element[(tan_index+3):])))
        elif("cot" in element):
            cot_index = element.index("cot")
            if(cot_index != 0):
                factor = float(element[:cot_index])
            temp_storage[index] = factor * math.cos(math.radians(float(element[(cot_index+3):])))/math.sin(math.radians(float(element[(cot_index+3):])))
        index = index + 1
    return solve(temp_storage)

#####   SOLVE
#vars
#def
def solve(temp_storage):
    val_storage = 0
    index = 0
    try:
        val_storage = float(temp_storage[index])
    except:
        log(["Invalid inputs", temp_storage])
        return "err"
    for element in temp_storage:
        if(element in operators):
            #PARSE ADDITION
            if(element == "+"):
                if(priorityCheck(temp_storage,index)):
                    print(val_storage, " + ", prioritySum(temp_storage,index))
                    val_storage = val_storage + prioritySum(temp_storage,index)
                    if(outOfBounds(temp_storage,index)):
                        break
                    else:
                        index = index + 4
                else:
                    print(val_storage, "+", temp_storage[index+1])
                    val_storage = val_storage + float(temp_storage[index+1])
            #PARSE SUBTRACTION
            elif(element == "-"):
                #   Debug progress check
                if(priorityCheck(temp_storage,index)):
                    print(val_storage, " - ", prioritySum(temp_storage,index))
                    val_storage = val_storage - prioritySum(temp_storage,index)
                    if(outOfBounds(temp_storage,index)):
                        break
                    else:
                        index = index + 4
                else:
                    print(val_storage, "-", temp_storage[index+1])
                    val_storage = val_storage - float(temp_storage[index+1])
            #PARSE MULTIPLICATION
            elif(element == "*"):
                #   Debug progress check
                print(val_storage, "*", temp_storage[index+1])
                #
                val_storage = val_storage * float(temp_storage[index+1])
            #PARSE DIVISION
            elif(element == "/"):
                #   Debug progress check
                print(val_storage, "/", temp_storage[index+1])
                #
                val_storage = val_storage / float(temp_storage[index+1])
            #HANDLE END OF EXPRESSION
            elif(element == ''):
                return val_storage
        index = index + 1
    return val_storage

##### priorityCheck
#vars
#def
def priorityCheck(temp_storage,index):
    if(temp_storage[index+2]=="*" or temp_storage[index+2]=="/"):
        return True

##### prioritySum
#vars
#def
def prioritySum(temp_storage,index):
    if(temp_storage[index+2] == "*"):
        sum = float(temp_storage[index+3])*float(temp_storage[index+1])
        print(temp_storage[index+3]," * ",temp_storage[index+1])
    else:
        sum = float(temp_storage[index+3])/float(temp_storage[index+1])
        print(temp_storage[index+3]," / ",temp_storage[index+1])
    return sum

##### outOfBounds
#vars
#def
def outOfBounds(temp_storage,index):
    if(temp_storage[index+4]==''):
        return True

##### log
#vars
#def
def log(args):
    for element in args:
        print(">",element, end =" ")
    print("")
