#imports
import math
#####   INTERPRET
#vars
operators = ["+","-","*",'/']
#def
def interpret(args,ans):
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
        elif("ans" in element):
            ans_index = element.index("ans")
            if(ans_index != 0):
                factor = float(element[:ans_index])
            temp_storage[index] = factor * float(ans)
        index = index + 1
    #return solved expression to JS
    return solve(temp_storage,ans)

#####   SOLVE
#vars
#def
def solve(temp_storage,ans):
    #strip blank space from temp_storage and add blank space to end for end of expression
    temp_storage[:] = (value for value in temp_storage if value != '')
    temp_storage.append('')
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
    val_storage = float(temp_storage[0])
    index = 0
    for element in temp_storage:
        if(element == '+'):
            val_storage = val_storage + float(temp_storage[index+1])
        elif(element == '-'):
            val_storage = val_storage - float(temp_storage[index+1])
        index = index + 1
    return val_storage

##### log
#vars
#def
def log(args):
    for element in args:
        print(">",element, end =" ")
    print("")
