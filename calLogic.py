#imports
#####   INTERPRET
#vars
operators = ["+","-","*",'/']
#def
def interpret(args):
    tempStorage = ['']*32
    index = 0
    result = list(args)
    for element in result:
        if(element in operators):
            index = index + 1
            tempStorage[index] = element
            index = index + 1
        else:
            tempStorage[index] = tempStorage[index]+element
            # print("Temp loop 2: ",tempStorage)

    return solve(tempStorage)
#####   SOLVE
#vars
#def
def solve(tempStorage):
    valStorage = 0
    index = 0
    valStorage = int(tempStorage[index])
    print("ValStorage step 0", valStorage)
    print("tempStorage status: ", tempStorage)
    for element in tempStorage:
        if(element in operators):
            if(element == "+"):
                print("Index at operator detection: ",index)
                if(priorityCheck(tempStorage,index)):
                    print(valStorage, " + ", prioritySum(tempStorage,index))
                    valStorage = valStorage + prioritySum(tempStorage,index)
                    if(outOfBounds(tempStorage,index)):
                        break
                    else:
                        index = index + 4
                    print("Index at priority check", index)
                else:
                    print(valStorage, "+", tempStorage[index+1])
                    valStorage = valStorage + int(tempStorage[index+1])
            elif(element == "-"):
                #   Debug progress check
                if(priorityCheck(tempStorage,index)):
                    print(valStorage, " - ", prioritySum(tempStorage,index))
                    valStorage = valStorage - prioritySum(tempStorage,index)
                    if(outOfBounds(tempStorage,index)):
                        break
                    else:
                        index = index + 4
                    print("Index at priority check", index)
                else:
                    print(valStorage, "-", tempStorage[index+1])
                    valStorage = valStorage - int(tempStorage[index+1])
            elif(element == "*"):
                #   Debug progress check
                print(valStorage, "*", tempStorage[index+1])
                #
                valStorage = valStorage * int(tempStorage[index+1])
            elif(element == "/"):
                #   Debug progress check
                print(valStorage, "/", tempStorage[index+1])
                #
                valStorage = valStorage / int(tempStorage[index+1])
            elif(element == ''):
                return valStorage
            print("Valstorage step final ", valStorage)
        index = index + 1
    return valStorage
##### priorityCheck
#vars
#def
def priorityCheck(tempStorage,index):
    if(tempStorage[index+2]=="*" or tempStorage[index+2]=="/"):
        return True

##### prioritySum
#vars
#def
def prioritySum(tempStorage,index):
    if(tempStorage[index+2] == "*"):
        sum = int(tempStorage[index+3])*int(tempStorage[index+1])
        print(tempStorage[index+3]," * ",tempStorage[index+1])
    else:
        sum = int(tempStorage[index+3])/int(tempStorage[index+1])
        print(tempStorage[index+3]," / ",tempStorage[index+1])
    return sum
##### outOfBounds
#vars
#def
def outOfBounds(tempStorage,index):
    if(tempStorage[index+4]==''):
        return True
