#         012345678901234
parrot = "Norwegian Blue"
print(parrot)
#challenge - using the characters from parrot string value print out we win through separate lines using indexing
print(parrot[3]) #w
print(parrot[4]) #e
print(parrot[9]) # space
print(parrot[3]) #w
print(parrot[6]) #i
print(parrot[8]) #n

# negative indexing
print()
print(parrot[-1])
print(parrot[-14])
# use indexing from line 5-10 to generate same answer with negative indexing
print()
print(parrot[-11]) #w
print(parrot[-10]) #e
print(parrot[-5]) # space
print(parrot[-11]) #w
print(parrot[-8]) #i
print(parrot[-6]) #n
#another solution is to add -14 inside each index
print()
print(parrot[3-14]) #w
print(parrot[4-14]) #e
print(parrot[9-14]) # space
print(parrot[3-14]) #w
print(parrot[6-14]) #i
print(parrot[8-14]) #n

slice

print(parrot[0:6])  # Noreg start at 0 stop at but not including position 6
print(parrot[3:5])  # we
print(parrot[0:9])  # Norwegian
print(parrot[:9])   # Norwegian - without providing starting value
print(parrot[10:14]) # Blue
# or - which i prefer
print(parrot[10:])  # Blue
print(parrot[:])    #when no start and or end values are provided, it will print the whole string


#negative slicing
print()
print(parrot[-4:-2])   # Bl
print(parrot[-4:12])   # Bl

print(parrot[-14:-8])

# addition - using steps
print()
print(parrot[0:6:2])    # nre from 0 up to but not including 6 every 2 steps
print(parrot[0:6:3])    # nw from 0 up to but not including 6 every 3 steps

number = "9,223;372:036 854,775;807"
print()
separators = number[1::4]
print(separators)

values = "".join(char if char not in separators else " " for char in number).split()

print([int(val) for val in values])
