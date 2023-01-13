# fileops.py

import calLogic as logic

#

def parseFile(file):
    results = []
    with open(file,"r") as read_file:
        for line in read_file:
            result = logic.interpret(line.rstrip().replace(" ",""))
            results.append(result)

    return results
