#####trig.py
# Return accurate results from trig functions
# Takes degrees values by default
#
import math
#
def sin(args):
    args = float(args) #redundancy float conversion
    if(args%180==0):
        return float(0)
    else:
        return math.sin(math.radians(args))
#
def cos(args):
    args = float(args) #redundancy float conversion
    if(((args*2-180)/360).is_integer()):
        return float(0)
    else:
        return math.cos(math.radians(args))
#
def tan(args):
    args = float(args) #redundancy float conversion
    if(args%180==0):
        return float(0)
    elif(((args*2-180)/360).is_integer()):
        return "undefined"
    elif(((4*args-180)/720).is_integer()):
        return float(1)
    elif(((4*args-3*180)/720).is_integer()):
        return float(-1)
    else:
        return math.tan(math.radians(args))
#
def cot(args):
    args = float(args) #redundancy float conversion
    if(((args*2-180)/360).is_integer()):
        return float(0)
    elif(args%180==0):
        return "undefined"
    elif((4*args-180)/720).is_integer():
        return float(1)
    elif((4*args-3*180)/720).is_integer():
        return float(-1)
    else:
        return float(cos(args)/sin(args))
