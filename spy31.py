# functions
def my_func1():                   # def keyword is used to define a function
    print('you are in function')  # function body
    return 'shubham'              # function returns the value
my_func1()                        # function is called
v = my_func1()                    # function is calling and the value of function is stored in a variable
print(v)                          # value of function is printed

print()
# function arguments or parameter
def my_function(fname):           # argument=parameter is introduce inside parenthesis() i.e., fname
    print(fname + " parker")
my_function("peter")              # function is called with argument
my_function("tony")

print()
# arbitrary argument, *args
def my_function(*fname):           # * is used if you do not know the no. of arguments
    print(fname[0] + " parker")    # [0] is used to get the position of argument
    print(fname[1] + " parker")    # [1] is used to get the position of argument
my_function("peter", "tony")       # function is called with unlimited no. of arguments

print()
# arbitrary keyword argument, **kwargs
def my_function(**fname):                        # ** is used if you do not know the no. of keyword arguments
    print(fname["fname1"] + " parker")           # fname1/2 is the key which store some value(here is peter)
    print(fname["fname2"] + " parker")           # ["fname2"] is used to print the value stored in fname2
my_function(fname1="peter", fname2="tony")       # function is called with unlimited no. of keyword arguments

print()
# passing list as an argument
def my_function(food):
    for x in food:
        print(x)
fruits = ["apple", "banana", "cherry"]
my_function(fruits)
