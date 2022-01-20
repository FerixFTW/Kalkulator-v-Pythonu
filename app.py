import eel
import random
from datetime import datetime
#
eel.init('web')
#
@eel.expose
def parseInput(args):
    print(args)
    eel.callResult(30)
@eel.expose
#TODO: MOVE LOGIC COUNTER AND STORAGE TO JS
#      PASS LOGIC COUNTER AND STORAGE TO PYTHON THROUGH JS
#      AND RETURN LOGIC RESULT BACK TO JS TO DISPLAY
def logicParse(args):
    operators = ['+','-','/','*']
    try:
        print(logicCounter)
    except:
        print("Give me my shares back, fucko")
    print("Passing args ",args)
    if(args in operators):
        print("Operator detected")
        logicCounter+=1
        logicStorage[logicCounter]=args
        logicCounter+=1
    else:
        print("Appending")
        logicStorage[logicCounter] = logicStorage[logicCounter]+args
        print(logicStorage)

#vars
logicStorage = []
logicCounter = 0
#
eel.start('index.html')
