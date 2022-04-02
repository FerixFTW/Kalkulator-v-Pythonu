##### graphing.py
# File that handles graphing logic and presentation
# Meant to take same args as calLogic, works in tandem with it
#
import matplotlib.pyplot as plt
import numpy as np
import calLogic as logic
#get function roots - zeros
def zeros(exponents,factors,sum):
    factorsMatrix = [[0]*2 for i in range(len(exponents))]
    index = 0
    #take exponents and factor pairs and put them in a 2d arry
    for element in factorsMatrix:
        element[0] = exponents[index]
        element[1] = factors[index]
        index = index + 1
    #sort descending by exponent
    factorsMatrix.sort(key = lambda factorsMatrix:factorsMatrix[0], reverse=True)
    parsed_factors = [0]*int(factorsMatrix[0][0])
    parsed_factors[0]=(factorsMatrix[0][1])
    #prepare proper args for np.roots - check np.roots docs for context
    for element in factorsMatrix:
        tgt_index = int(factorsMatrix[0][0]-element[0])
        parsed_factors[tgt_index] = element[1]
    ##############################################
    parsed_factors.append(sum)
    zeros = np.roots(parsed_factors)
    result = []
    for intercept in zeros: #for each intercept append only real intercepts
        if not np.iscomplex(intercept):
            result.append(intercept)
    logic.debug([result])
    if not result: #if result is empty return None
        return None
    else: #else return the intercepts
        return result

#parse y from calculator
def parse_y(args):
    temp_storage = logic.parse_args(args)
    factors = []
    exponents = []
    index = 0
    for element in temp_storage:
        #x parsing and factor checking
        if "x" in element:
            x_index = element.index("x")
            if x_index == 0 and index==0:
                factor = 1.0
            elif x_index == 0 and index!=0:
                if temp_storage[index-1] == '-':
                    factor = -1.0
                else:
                    factor = 1
            elif x_index == 1 and index==0 and element[0]=='-':
                factor = -1.0
            else:
                #get factor
                factor = float(element[:x_index])
                if(len(temp_storage)>1): #check if there is anything beside x
                    #check if factor is supposed to be negative
                    if(index != 0 and temp_storage[index-1]=="-"):
                        factor = factor*-1
            #get exponent
            if "^" in element: #append explicit exponent
                exp_index = element.index("^")
                exp = float(element[(exp_index+1):])
                exponents.append(exp)
                factors.append(factor)
            else: #append default exponent - 1
                exponents.append(1.0)
                factors.append(factor)
            #set x element to 0 so normal math operations can take place
            x_element_index = temp_storage.index(element)
            temp_storage[x_element_index]="0"
        #
        index = index + 1
    sum = logic.interpret(temp_storage,0)
    ##### draw the actual graph ################################################
    #####
    fig, ax = plt.subplots()
    #move the left and bottom axes to x,y = 0
    ax.spines[["left", "bottom"]].set_position(("data", 0))
    #hide the top and right axes
    ax.spines[["top", "right"]].set_visible(False)
    #plot axes with arrowheads
    ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
    ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)
    #
    #finalise x and y declarations
    x = np.linspace(-30, 30, 1000)
    y = sum
    for index in range(len(exponents)):
        y = y + np.power(x,exponents[index])*factors[index]
    #draw intercepts
    plt.scatter(0,sum,s=50) #draw y axis intercept
    logic.debug(["function:",args])
    x_intercepts = zeros(exponents,factors,sum)
    if x_intercepts != None:
        for x_cord in x_intercepts:
            plt.scatter(x_cord,0,s=50) #draw x axis intercept(s)
    #finally draw graph
    ax.plot(x, y,'-r',label=args)
    plt.legend(loc='upper left')
    #
    return plt.show()
#
