#naredi logične operacije

################################## INTERNAL FNCS ###############################

def reverse(args):
    return args [::-1]

def sprOCT(args):
    switcher = {
        0:0,
        1:1,
        10:2,
        11:3,
        100:4,
        101:5,
        110:6,
        111:7
    }
    return switcher.get(args)

def sprHEX(args):
    switcher = {
        0: 0,
        1: 1,
        10: 2,
        11: 3,
        100: 4,
        101: 5,
        110: 6,
        111: 7,
        1000: 8,
        1001:9,
        1010:"A",
        1011:"B",
        1100:"C",
        1101:"D",
        1110:"E",
        1111:"F"
    }
    return switcher.get(args)

def sprOCTtoBIN(args):
    switcher = {
        0: "000",
        1: "001",
        2: "010",
        3: "011",
        4: 100,
        5: 101,
        6: 110,
        7: 111
    }
    return switcher.get(args)

def sprHEXtoBIN(args):
    switcher = {
        "0": "0000",
        "1": "0001",
        "2": "0010",
        "3": "0011",
        "4": "0100",
        "5": "0101",
        "6": "0110",
        "7": "0111",
        "8": "1000",
        "9": "1001",
        "A": "1010",
        "B": "1011",
        "C": "1100",
        "D": "1101",
        "E": "1110",
        "F": "1111"
    }
    return switcher.get(args)

################################## EXTERNAL FNCS ###############################

def pBIN(args):
    args = args.upper()
    if "A" in args or "B" in args or "C" in args or "D" in args or "E" in args or "F" in args:
        return "Napaka, številka ni v pravilnem številskem sistemu."
    else:
        x = ""
        args = int(args)
        while (args > 1):
            x+=str(args%2)
            args=int(args/2)
            if args<=1:
                break
        x+=str(args)
        return reverse(x)

def pOCT(args):
    args = args.upper()
    if "A" in args or "B" in args or "C" in args or "D" in args or "E" in args or "F" in args:
        return "Napaka, številka ni v pravilnem številskem sistemu."
    else:
        x = ""
        args = int(args)
        while (args > 7):
            x += str(args % 8)
            args = int(args / 8)
            if args <= 7:
                break
        x += str(args)
        return reverse(x)

def pHEX(args):
    args = args.upper()
    if "A" in args or "B" in args or "C" in args or "D" in args or "E" in args or "F" in args:
        return "Napaka, številka ni v pravilnem številskem sistemu."
    else:
        args = eval(args)
        x = ""
        while args > 15:
            y = str(args % 16)
            if y == "15":
                x += "F"
            elif y == "14":
                x += "E"
            elif y == "13":
                x += "D"
            elif y == "12":
                x += "C"
            elif y == "11":
                x += "B"
            elif y == "10":
                x += "A"
            else:
                x += y
            args = int(args / 16)
        if args == 15:
            x += "F"
        elif args == 14:
            x += "E"
        elif args == 13:
            x += "D"
        elif args == 12:
            x += "C"
        elif args == 11:
            x += "B"
        elif args == 10:
            x += "A"
        else:
            x += str(args)
        return reverse(x)

def BtoOCT(args):
    args = args.upper()
    if "2" in args or "3" in args or "4" in args or "5" in args or "6" in args or "7" in args or "8" in args or "9" in args or "A" in args or "B" in args or "C" in args or "D" in args or "E" in args or "F" in args:
        return "Napaka, številka ni v pravilnem številskem sistemu."
    args = int(args)
    if args==0:
        return 0
    else:
        z=""
        while(args!=0):
            x=args%1000
            z+=str(sprOCT(x))
            args//=1000
        return reverse(z)

def BtoDEC(args):
    args = args.upper()
    if "2" in args or "3" in args or "4" in args or "5" in args or "6" in args or "7" in args or "8" in args or "9" in args or "A" in args or "B" in args or "C" in args or "D" in args or "E" in args or "F" in args:
        return "Napaka, številka ni v pravilnem številskem sistemu."
    else:
        args = int(args)
        z = 0
        utez = 1
        if args == 0:
            return 0
        while args != 0:
            x = args % 10
            z += x * utez
            utez *= 2
            args //= 10
        return z

def BtoHEX(args):
    args = args.upper()
    if "2" in args or "3" in args or "4" in args or "5" in args or "6" in args or "7" in args or "8" in args or "9" in args or "A" in args or "B" in args or "C" in args or "D" in args or "E" in args or "F" in args:
        return "Napaka, številka ni v pravilnem številskem sistemu."
    else:
        z = ""
        args = int(args)
        if args == 0:
            return "0"
        while (args != 0):
            x = args % 10000
            z += str(sprHEX(x))
            args //= 10000
        return reverse(z)

def OtoBIN(args):
    args = args.upper()
    if "8" in args or "9" in args or "A" in args or "B" in args or "C" in args or "D" in args or "E" in args or "F" in args:
        return "Napaka, številka ni v pravilnem številskem sistemu."
    else:
        z = ""
        args = int(args)
        if args == 0:
            return "0"
        while args != 0:
            x = args % 10
            z = str(sprOCTtoBIN(x)) + z
            args //= 10
        return z

def OtoDEC(args):
    args = args.upper()
    if "8" in args or "9" in args or "A" in args or "B" in args or "C" in args or "D" in args or "E" in args or "F" in args:
        return "Napaka, številka ni v pravilnem številskem sistemu."
    else:
        z = 0
        utez = 1
        args = int(args)
        if args == 0:
            return 0
        while args != 0:
            x = args % 10
            z += x * utez
            utez *= 8
            args //= 10
        return z

def OtoHEX(args):
    args = args.upper()
    if "8" in args or "9" in args or "A" in args or "B" in args or "C" in args or "D" in args or "E" in args or "F" in args:
        return "Napaka, številka ni v pravilnem številskem sistemu."
    else:
        args = OtoBIN(args)
        return BtoHEX(args)

def HtoBIN(args):
    args = args.upper()
    z = ""
    for i in range(len(args)):
        x = args[len(args) - i - 1:len(args) - i]
        z = sprHEXtoBIN(x) + z
        args = args[:len(args)]
    return z

def HtoOCT(args):
    args = args.upper()
    args = HtoBIN(args)
    return BtoOCT(args)

def HtoDEC(args):
    args = args.upper()
    utez = 1
    z = 0
    for i in range(len(args)):
        x = args[len(args) - i - 1:len(args) - i]
        if x == "A":
            z += 10 * utez
        elif x == "B":
            z += 11 * utez
        elif x == "C":
            z += 12 * utez
        elif x == "D":
            z += 13 * utez
        elif x == "E":
            z += 14 * utez
        elif x == "F":
            z += 15 * utez
        else:
            z += eval(x) * utez
        utez *= 16
    return z

################################### LOGIC OPS ##################################

### BIN LOGIC

def BIN_AND(st1,st2):
    st1.upper()
    st2.upper()
    if "2" in st1 or "3" in st1 or "4" in st1 or "5" in st1 or "6" in st1 or "7" in st1 or "8" in st1 or "9" in st1 or "A" in st1 or "B" in st1 or "C" in st1 or "D" in st1 or "E" in st1 or "F" in st1 or "2" in st2 or "3" in st2 or "4" in st2 or "5" in st2 or "6" in st2 or "7" in st2 or "8" in st2 or "9" in st2 or "A" in st2 or "B" in st2 or "C" in st2 or "D" in st2 or "E" in st2 or "F" in st2:
        return "Napaka, številka ni v pravilnem številskem sistemu."
    else:
        a = len(st1)
        b = len(st2)
        if a == b:
            z = ""
            for i in range(len(st1)):
                x = st1[len(st1) - i - 1:len(st1) - i]
                y = st2[len(st2) - i - 1:len(st2) - i]
                if x == "1" and y == "1":
                    z = "1"+z
                else:
                    z = "0"+z
            return z
        else:
            while a != b:
                if a > b:
                    st2 = "0"+st2
                    b = len(st2)
                else:
                    st1 = "0"+st1
                    a = len(st1)
            z = ""
            for i in range(len(st1)):
                x = st1[len(st1) - i - 1:len(st1) - i]
                y = st2[len(st2) - i - 1:len(st2) - i]
                if x == "1" and y == "1":
                    z = "1" + z
                else:
                    z = "0" + z
            return z

def BIN_OR(st1,st2):
    st1.upper()
    st2.upper()
    if "2" in st1 or "3" in st1 or "4" in st1 or "5" in st1 or "6" in st1 or "7" in st1 or "8" in st1 or "9" in st1 or "A" in st1 or "B" in st1 or "C" in st1 or "D" in st1 or "E" in st1 or "F" in st1 or "2" in st2 or "3" in st2 or "4" in st2 or "5" in st2 or "6" in st2 or "7" in st2 or "8" in st2 or "9" in st2 or "A" in st2 or "B" in st2 or "C" in st2 or "D" in st2 or "E" in st2 or "F" in st2:
        return "Napaka, številka ni v pravilnem številskem sistemu."
    else:
        a = len(st1)
        b = len(st2)
        if a == b:
            z = ""
            for i in range(len(st1)):
                x = st1[len(st1) - i - 1:len(st1) - i]
                y = st2[len(st2) - i - 1:len(st2) - i]
                if x == "0" and y == "0":
                    z = "0" + z
                else:
                    z = "1" + z
            return z
        else:
            while a != b:
                if a > b:
                    st2 = "0" + st2
                    b = len(st2)
                else:
                    st1 = "0" + st1
                    a = len(st1)
            z = ""
            for i in range(len(st1)):
                x = st1[len(st1) - i - 1:len(st1) - i]
                y = st2[len(st2) - i - 1:len(st2) - i]
                if x == "0" and y == "0":
                    z = "0" + z
                else:
                    z = "1" + z
            return z

def BIN_NOT(st1):
    st1.upper()
    if "2" in st1 or "3" in st1 or "4" in st1 or "5" in st1 or "6" in st1 or "7" in st1 or "8" in st1 or "9" in st1 or "A" in st1 or "B" in st1 or "C" in st1 or "D" in st1 or "E" in st1 or "F" in st1:
        return "Napaka, številka ni v pravilnem številskem sistemu."
    else:
        z = ""
        for i in range(len(st1)):
            x = st1[len(st1) - i - 1:len(st1) - i]
            if x == "0":
                z = "1" + z
            else:
                z = "0" + z
        return z

def BIN_NOR(st1,st2):
    st1.upper()
    st2.upper()
    if "2" in st1 or "3" in st1 or "4" in st1 or "5" in st1 or "6" in st1 or "7" in st1 or "8" in st1 or "9" in st1 or "A" in st1 or "B" in st1 or "C" in st1 or "D" in st1 or "E" in st1 or "F" in st1 or "2" in st2 or "3" in st2 or "4" in st2 or "5" in st2 or "6" in st2 or "7" in st2 or "8" in st2 or "9" in st2 or "A" in st2 or "B" in st2 or "C" in st2 or "D" in st2 or "E" in st2 or "F" in st2:
        return "Napaka, številka ni v pravilnem številskem sistemu."
    else:
        a = len(st1)
        b = len(st2)
        if a == b:
            z = ""
            for i in range(len(st1)):
                x = st1[len(st1) - i - 1:len(st1) - i]
                y = st2[len(st2) - i - 1:len(st2) - i]
                if x == "0" and y == "0":
                    z = "1" + z
                else:
                    z = "0" + z
            return z
        else:
            while a != b:
                if a > b:
                    st2 = "0" + st2
                    b = len(st2)
                else:
                    st1 = "0" + st1
                    a = len(st1)
            z = ""
            for i in range(len(st1)):
                x = st1[len(st1) - i - 1:len(st1) - i]
                y = st2[len(st2) - i - 1:len(st2) - i]
                if x == "0" and y == "0":
                    z = "1" + z
                else:
                    z = "0" + z
            return z

def BIN_NAND(st1,st2):
    st1.upper()
    st2.upper()
    if "2" in st1 or "3" in st1 or "4" in st1 or "5" in st1 or "6" in st1 or "7" in st1 or "8" in st1 or "9" in st1 or "A" in st1 or "B" in st1 or "C" in st1 or "D" in st1 or "E" in st1 or "F" in st1 or "2" in st2 or "3" in st2 or "4" in st2 or "5" in st2 or "6" in st2 or "7" in st2 or "8" in st2 or "9" in st2 or "A" in st2 or "B" in st2 or "C" in st2 or "D" in st2 or "E" in st2 or "F" in st2:
        return "Napaka, številka ni v pravilnem številskem sistemu."
    else:
        a = len(st1)
        b = len(st2)
        if a == b:
            z = ""
            for i in range(len(st1)):
                x = st1[len(st1) - i - 1:len(st1) - i]
                y = st2[len(st2) - i - 1:len(st2) - i]
                if x == "1" and y == "1":
                    z = "0" + z
                else:
                    z = "1" + z
            return z
        else:
            while a != b:
                if a > b:
                    st2 = "0" + st2
                    b = len(st2)
                else:
                    st1 = "0" + st1
                    a = len(st1)
            z = ""
            for i in range(len(st1)):
                x = st1[len(st1) - i - 1:len(st1) - i]
                y = st2[len(st2) - i - 1:len(st2) - i]
                if x == "1" and y == "1":
                    z = "0" + z
                else:
                    z = "1" + z
            return z

def BIN_XOR(st1,st2):
    st1.upper()
    st2.upper()
    if "2" in st1 or "3" in st1 or "4" in st1 or "5" in st1 or "6" in st1 or "7" in st1 or "8" in st1 or "9" in st1 or "A" in st1 or "B" in st1 or "C" in st1 or "D" in st1 or "E" in st1 or "F" in st1 or "2" in st2 or "3" in st2 or "4" in st2 or "5" in st2 or "6" in st2 or "7" in st2 or "8" in st2 or "9" in st2 or "A" in st2 or "B" in st2 or "C" in st2 or "D" in st2 or "E" in st2 or "F" in st2:
        return "Napaka, številka ni v pravilnem številskem sistemu."
    else:
        a = len(st1)
        b = len(st2)
        if a == b:
            z = ""
            for i in range(len(st1)):
                x = st1[len(st1) - i - 1:len(st1) - i]
                y = st2[len(st2) - i - 1:len(st2) - i]
                if x == y:
                    z = "0" + z
                else:
                    z = "1" + z
            return z
        else:
            while a != b:
                if a > b:
                    st2 = "0" + st2
                    b = len(st2)
                else:
                    st1 = "0" + st1
                    a = len(st1)
            z = ""
            for i in range(len(st1)):
                x = st1[len(st1) - i - 1:len(st1) - i]
                y = st2[len(st2) - i - 1:len(st2) - i]
                if x == y:
                    z = "0" + z
                else:
                    z = "1" + z
            return z

def BIN_XNOR(st1,st2):
    st1.upper()
    st2.upper()
    if "2" in st1 or "3" in st1 or "4" in st1 or "5" in st1 or "6" in st1 or "7" in st1 or "8" in st1 or "9" in st1 or "A" in st1 or "B" in st1 or "C" in st1 or "D" in st1 or "E" in st1 or "F" in st1 or "2" in st2 or "3" in st2 or "4" in st2 or "5" in st2 or "6" in st2 or "7" in st2 or "8" in st2 or "9" in st2 or "A" in st2 or "B" in st2 or "C" in st2 or "D" in st2 or "E" in st2 or "F" in st2:
        return "Napaka, številka ni v pravilnem številskem sistemu."
    else:
        a = len(st1)
        b = len(st2)
        if a == b:
            z = ""
            for i in range(len(st1)):
                x = st1[len(st1) - i - 1:len(st1) - i]
                y = st2[len(st2) - i - 1:len(st2) - i]
                if x == y:
                    z = "1" + z
                else:
                    z = "0" + z
            return z
        else:
            while a != b:
                if a > b:
                    st2 = "0" + st2
                    b = len(st2)
                else:
                    st1 = "0" + st1
                    a = len(st1)
            z = ""
            for i in range(len(st1)):
                x = st1[len(st1) - i - 1:len(st1) - i]
                y = st2[len(st2) - i - 1:len(st2) - i]
                if x == y:
                    z = "1" + z
                else:
                    z = "0" + z
            return z

### OCT LOGIC

def OCT_AND(st1,st2):
    st1 = OtoBIN(st1)
    st2 = OtoBIN(st2)
    return BtoOCT(BIN_AND(st1, st2))

def OCT_OR(st1,st2):
    st1 = OtoBIN(st1)
    st2 = OtoBIN(st2)
    return BtoOCT(BIN_OR(st1, st2))

def OCT_NOT(st1):
    st1 = OtoBIN(st1)
    return BtoOCT(BIN_NOT(st1))

def OCT_NOR(st1,st2):
    st1 = OtoBIN(st1)
    st2 = OtoBIN(st2)
    return BtoOCT(BIN_NOR(st1, st2))

def OCT_NAND(st1,st2):
    st1 = OtoBIN(st1)
    st2 = OtoBIN(st2)
    return BtoOCT(BIN_NAND(st1, st2))

def OCT_XOR(st1,st2):
    st1 = OtoBIN(st1)
    st2 = OtoBIN(st2)
    return BtoOCT(BIN_XOR(st1, st2))

def OCT_XNOR(st1,st2):
    st1 = OtoBIN(st1)
    st2 = OtoBIN(st2)
    return BtoOCT(BIN_XNOR(st1, st2))

### DEC LOGIC

def DEC_AND(st1, st2):
    st1 = pBIN(st1)
    st2 = pBIN(st2)
    return BtoDEC(BIN_AND(st1, st2))

def DEC_OR(st1, st2):
    st1 = pBIN(st1)
    st2 = pBIN(st2)
    return BtoDEC(BIN_OR(st1, st2))

def DEC_NOT(st1):
    st1 = pBIN(st1)
    return BtoDEC(BIN_NOT(st1))

def DEC_NAND(st1, st2):
    st1 = pBIN(st1)
    st2 = pBIN(st2)
    return BtoDEC(BIN_NAND(st1, st2))

def DEC_NOR(st1, st2):
    st1 = pBIN(st1)
    st2 = pBIN(st2)
    return BtoDEC(BIN_NOR(st1, st2))

def DEC_XOR(st1, st2):
    st1 = pBIN(st1)
    st2 = pBIN(st2)
    return BtoDEC(BIN_XOR(st1, st2))

def DEC_XNOR(st1, st2):
    st1 = pBIN(st1)
    st2 = pBIN(st2)
    return BtoDEC(BIN_XNOR(st1, st2))

### HEX LOGIC

def HEX_AND(st1, st2):
    st1 = HtoBIN(st1)
    st2 = HtoBIN(st2)
    return BtoHEX(BIN_AND(st1, st2))

def HEX_OR(st1, st2):
    st1 = HtoBIN(st1)
    st2 = HtoBIN(st2)
    return BtoHEX(BIN_OR(st1, st2))

def HEX_NOT(st1):
    st1 = HtoBIN(st1)
    return BtoHEX(BIN_NOT(st1))

def HEX_NAND(st1, st2):
    st1 = HtoBIN(st1)
    st2 = HtoBIN(st2)
    return BtoHEX(BIN_NAND(st1, st2))

def HEX_NOR(st1, st2):
    st1 = HtoBIN(st1)
    st2 = HtoBIN(st2)
    return BtoHEX(BIN_NOR(st1, st2))

def HEX_XOR(st1, st2):
    st1 = HtoBIN(st1)
    st2 = HtoBIN(st2)
    return BtoHEX(BIN_XOR(st1, st2))

def HEX_XNOR(st1, st2):
    st1 = HtoBIN(st1)
    st2 = HtoBIN(st2)
    return BtoHEX(BIN_XNOR(st1, st2))
