
# functions can have arguments and parameters

# x, y, z are parameters - unknown
def multiply(x, y ,z):
    #x = 4
    #y = 6
    #z = 7
    answer = x * y *z
    print('Product is ', answer)

# below x, y z are arguments
multiply(x = 5, y = 8, z = 9)
multiply(x = 4, y = 9, z = 3)
multiply(x = 1, y = 10, z = 3)

# find area1/2bh
# b and h are said to be params
def area(b, h):
    #b = 45
    #h = 2
    answer = 1/2 * b*h
    print('Area is ', answer)

# below b abd h are said to args
area(b = 5, h = 5)
area(b = 4, h = 2)
area(b = 5, h = 10)


