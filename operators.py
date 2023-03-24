a = 12
b = 3

print(a + b)    # 15
print(a - b)    # 9
print(a * b)    # 36
print(a / b)    # 4.0 - inputs a float result
print(a // b)   # 4 - integer division - rounded down to minus infinity
print(a % b)    # modular: remainder after integer division

print()
#  for in range only allows you to input integer division //
# for i in range(1,a / b):
#     print(i)
# for above inputs TypeError: 'float' object cannot be interpreted as an integer
# for below is using the double / (//) for integer division to be calculated by the for in range

print(a + b / 3 - 4 * 12)

print()
print(a / (b * a) / b)
