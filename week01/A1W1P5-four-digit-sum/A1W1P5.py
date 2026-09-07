# Develop a program that reads a four-digit integer from the user and displays the sum of the digits in the number.
# Input example:
# 3141
# Output example:
# 3+1+4+1=9

# input
user_input = input("Please give a four-digit integer: ")

# processing
split_integer = (
    user_input[0] + "+" + user_input[1] + "+" + user_input[2] + "+" + user_input[3]
)

sum_integer = (
    int(user_input[0]) + int(user_input[1]) + int(user_input[2]) + int(user_input[3])
)

# output
print(user_input, "contains the following sum of digits:")
print(split_integer, "=", sum_integer)


### Oefenen
# woord = "kat"
# print(woord[0])
# print(woord[1])
# print(woord[2])

# print(woord[3])
# string index out of range

# getal = 1234
# print(getal[0])
# gaat niet want in 1 getal kan je niet prikken []

# dit werkt omdat het allemaal strings zijn!
# getal = input("Geef een viercijferig getal:")
# print(getal[0] + "+" +
#      getal[1] + "+" +
#      getal[2] + "+" +
#      getal[3])
# print(int(getal[0]) + int(getal[1]) + int(getal[2]) + int(getal[3]))

# woord = "kat"
# print(f"{woord[0]} is de eerste letter")


### volgende keer
# digits opsplitsen; digit1 = int(user_input[0]) etc. dan doet elke regel maar 1 ding
