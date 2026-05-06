'''
Outputs: 
- a list of rides
'''

age = int(input("Age:"))
day_of_week = input("Day of week:")
height = int(input("height in inches:"))
vip = input("VIP? yes/no").lower()
signed_waiver = input("Signed waiver? yes/no ").lower()
parent_present = input("Parent present? yes/no ")

# MegaDrop
if age >= 14 and signed_waiver == "yes" and (height >= 54 or (vip == "yes" and height >=50)):
    print("MegaDrop")

if age >= 14 and signed_waiver == "yes":
    if height >= 54:
        print("MegaDrop")
    elif vip == "yes" and height >= 50:
        print("MegaDrop")

# Thudnerbolt
if age >= 10 and height >=48 and day_of_week != "monday":
    print("Thunderboly")

# Kiddie
if age > 8 and parent_present == "yes":
    print("Kiddie")
    