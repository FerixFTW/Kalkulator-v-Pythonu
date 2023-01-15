# convert.py
# Linker between calLogic and ziga.py

import ziga

#

def parse_conversion(source, number, target):
    print("Called parse_conversion, convert.py")
    if(source == "BIN"):
        if(target == "OCT"):
            print("Called BIN to OCT")
            return ziga.BtoOCT(number)
        if(target == "DEC"):
            print("Called BIN to DEC")
            return ziga.BtoDEC(number)
        if(target == "HEX"):
            print("Called BIN to HEX")
            return ziga.BtoHEX(number)
        #else return error?
    if(source == "OCT"):
        if(target == "BIN"):
            print("Called OCT to BIN")
            return ziga.OtoBIN(number)
        if(target == "DEC"):
            print("Called OCT to DEC")
            return ziga.OtoDEC(number)
        if(target == "HEX"):
            print("Called OCT to HEX")
            return ziga.OtoHEX(number)
        #else return error?
    if(source == "HEX"):
        if(target == "BIN"):
            print("Called HEX to DEC")
            return ziga.HtoBIN(number)
        if(target == "OCT"):
            print("Called HEX to OCT")
            return ziga.HtoOCT(number)
        if(target == "DEC"):
            print("Called HEX to DEC")
            return ziga.HtoDEC(number)
        #else return error?
    if(source == "DEC"):
        if(target == "BIN"):
            print("Called DEC to BIN")
            return ziga.pBIN(number)
        if(target == "OCT"):
            print("Called DEC to OCT")
            return ziga.pOCT(number)
        if(target == "HEX"):
            print("Called DEC to HEX")
            return ziga.pHEX(number)
