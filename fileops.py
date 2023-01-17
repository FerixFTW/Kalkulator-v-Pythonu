# fileops.py

import calLogic as logic

#

def parseFile(file):
    results = []
    last_ans = 0
    with open(file,"r") as read_file:
        for line in read_file:
            result = logic.interpret(line.replace("=","").rstrip(),last_ans)
            last_ans = result
            results.append(result)

    return results
