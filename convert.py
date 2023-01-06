# convert.py
## ORG_SYSTEM number TGT_SYSTEM

number = 0
origin_system = ""
target_system = ""
allowed_systems = ["BIN","HEX","OCT","DEC"]

while (origin_system not in allowed_systems) and (target_system not in allowed_systems):
    if((origin_system or target_system) != ""):
        print("Allowed systems include: BIN,HEX,OCT,DEC")

    origin_system = str(input("Origin system: "))
    number = str(input("Number: "))
    target_system = str(input("Target system: "))

def bin_to_dec(bin_number):
    counter = 0
    for number in reversed(bin_number):
        print(number)

bin_to_dec("011")
