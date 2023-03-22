splitString = "This string has been\nsplit over\nseveral\nlines"
# \n starts new line
print(splitString)

tabbedString = "1\t2\t3\t4\t5"
print(tabbedString)

print('The pet show owner said "No, no, \'e\'s uh,..he\'s resting".')
#  or
print("The pet shop owner said \"No, no, 'e's uh,...he's resting\".")

print("""The Pet show owner said "No, no, 'e's uh,...he's resting". """)

anotherSplitString = """This string has been \
split over \
several \
lines"""

print(anotherSplitString)
# including backslash \")
# applying n additiobal backlash will escape the backlash - preferred
print("C:\\Users\\tuancarlosgomez\\notes.txt")
# adding r for raw before "" will remove the backlash behavior
print(r"C:\Users\tuancarlosgomez\notes.txt")
