#
import matplotlib.pyplot as plt
import numpy as np
#parse y from calculator
# TODO: Crunch sums/subtractions to a single value and add it to y at the end.
#       Be able to parse x exponents
#       Somehow utilise calLogic? 
def parse_y(args):
    fig, ax = plt.subplots()
    #move the left and bottom spines to x = 0 and y = 0, respectively.
    ax.spines[["left", "bottom"]].set_position(("data", 0))
    #hide the top and right spines.
    ax.spines[["top", "right"]].set_visible(False)
    #
    ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
    ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)
    #
    #parse y from calculator
    operators = ["+","-","*",'/']
    temp_storage = ['']*32
    result = list(args)
    #separate values from operators
    index = 0
    for element in result:
        if(element in operators):
            index = index + 1
            temp_storage[index] = element
            index = index + 1
        else:
            temp_storage[index] = temp_storage[index]+element
    #strip whitespace
    temp_storage[:] = (value for value in temp_storage if value != '')
    #get factors
    factor = 1
    for element in temp_storage:
        if "x" in element:
            x_index = element.index("x")
            if x_index == 0:
                factor = 1
            else:
                factor = float(element[:x_index])
    ##### draw the actual graph
    #draw graph x interval
    x = np.linspace(-10, 10, 400)
    #
    y = factor*x
    ax.plot(x, y,'-r',label=args)
    plt.legend(loc='upper left')
    #
    return plt.show()
#
