# Write a program that asks the user to enter the width and length of a room.
# Once the values have been read, your program should compute and display the area of the room.
# Criteria:

#    The length and the width need to be processed as floating point numbers

# Input example:

# Width: 5
# Length: 5.5
# Output example:

# The Area of the Room: 27.5

length = float(input("To calculate an area, first, please input length: "))
width = float(input("Next, please input width: "))


# calculation
area = length * width

print("The area of the room:", area)
