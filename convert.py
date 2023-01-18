# convert.py
# Linker between calLogic and ziga.py
# Handle system conversions and logic operations

import ziga

# private functions

def negate(system, number):

    if system == "BIN":
        return ziga.BIN_NOT(number)
    if system == "OCT":
        return ziga.OCT_NOT(number)
    if system == "DEC":
        return ziga.DEC_NOT(number)
    if system == "HEX":
        return ziga.HEX_NOT(number)

    return "invalid call"

def solve_operation(args):
    system = args[0].upper()
    first_number = args[1]
    second_number = args[3]
    operation = args[2].upper()

    if system == "BIN":
        if operation == "AND":
            return ziga.BIN_AND(first_number,second_number)
        if operation == "OR":
            return ziga.BIN_OR(first_number,second_number)
        if operation == "NOR":
            return ziga.BIN_NOR(first_number,second_number)
        if operation == "NAND":
            return ziga.BIN_NAND(first_number,second_number)
        if operation == "XOR":
            return ziga.BIN_XOR(first_number,second_number)
        if operation == "XNOR":
            return ziga.BIN_XNOR(first_number,second_number)
    if system == "OCT":
        if operation == "AND":
            return ziga.OCT_AND(first_number,second_number)
        if operation == "OR":
            return ziga.OCT_OR(first_number,second_number)
        if operation == "NOR":
            return ziga.OCT_NOR(first_number,second_number)
        if operation == "NAND":
            return ziga.OCT_NAND(first_number,second_number)
        if operation == "XOR":
            return ziga.OCT_XOR(first_number,second_number)
        if operation == "XNOR":
            return ziga.OCT_XNOR(first_number,second_number)
    if system == "DEC":
        if operation == "AND":
            return ziga.DEC_AND(first_number,second_number)
        if operation == "OR":
            return ziga.DEC_OR(first_number,second_number)
        if operation == "NOR":
            return ziga.DEC_NOR(first_number,second_number)
        if operation == "NAND":
            return ziga.DEC_NAND(first_number,second_number)
        if operation == "XOR":
            return ziga.DEC_XOR(first_number,second_number)
        if operation == "XNOR":
            return ziga.DEC_XNOR(first_number,second_number)
    if system == "HEX":
        if operation == "AND":
            return ziga.HEX_AND(first_number,second_number)
        if operation == "OR":
            return ziga.HEX_OR(first_number,second_number)
        if operation == "NOR":
            return ziga.HEX_NOR(first_number,second_number)
        if operation == "NAND":
            return ziga.HEX_NAND(first_number,second_number)
        if operation == "XOR":
            return ziga.HEX_XOR(first_number,second_number)
        if operation == "XNOR":
            return ziga.HEX_XNOR(first_number,second_number)

# public functions

def parse_conversion(temp_args):
    source = temp_args[0].upper()
    number = temp_args[1]
    target = temp_args[2].upper()

    if(source == "BIN"):
        if(target == "OCT"):
            return ziga.BtoOCT(number)
        if(target == "DEC"):
            return ziga.BtoDEC(number)
        if(target == "HEX"):
            return ziga.BtoHEX(number)
        #else return error?
    if(source == "OCT"):
        if(target == "BIN"):
            return ziga.OtoBIN(number)
        if(target == "DEC"):
            return ziga.OtoDEC(number)
        if(target == "HEX"):
            return ziga.OtoHEX(number)
        #else return error?
    if(source == "HEX"):
        if(target == "BIN"):
            return ziga.HtoBIN(number)
        if(target == "OCT"):
            return ziga.HtoOCT(number)
        if(target == "DEC"):
            return ziga.HtoDEC(number)
        #else return error?
    if(source == "DEC"):
        if(target == "BIN"):
            return ziga.pBIN(number)
        if(target == "OCT"):
            return ziga.pOCT(number)
        if(target == "HEX"):
            return ziga.pHEX(number)

def parse_operation(temp_args):
    #evaluate num_system and whether our numbers are negated
    num_system  = temp_args[0].upper()
    negate_first = temp_args[1].upper()=="NOT"

    if(negate_first):
        negate_second = temp_args[4].upper()=="NOT"
    else:
        negate_second = temp_args[3].upper()=="NOT"

    #evaluate our operator and numbers based on negations
    operator = temp_args[2]
    first_number = temp_args[1]

    if(negate_first):
        operator = temp_args[3]
        first_number = temp_args[2]

    second_number = temp_args[3]
    if(negate_first and negate_second):
        second_number = temp_args[5]
    elif((not negate_first and negate_second) or (negate_first and not negate_second)):
        second_number = temp_args[4]

    #negations and numbers found, now reduce negations
    parsed_args = [num_system]

    if(negate_first):
        parsed_args.append(negate(num_system,first_number))
    else:
        parsed_args.append(first_number)

    parsed_args.append(operator)

    if(negate_second):
        parsed_args.append(negate(num_system,second_number))
    else:
        parsed_args.append(second_number)

    #solve parsed_args and return to frontend
    result = solve_operation(parsed_args)

    return result
