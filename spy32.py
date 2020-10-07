# docstring
def my_func1():
    """this is first string"""  # docstring
    return 0
print(my_func1.__doc__)

print()
# global/local variable or global/local scope
var1 = 6                        # var1 is a global variable having global scope(approach)
def func1():
    print(var1)
    var2 = 3                    # var2 is a local variable having local scope(limited in its function only)
    print(var2)
func1()
print(var1)
# print(var2)                   # here it will through an error because var2 is a local variable

print()
def func2():
    global var1                 # here we use global keyword which allow the function to make changes in global variable
    var1 = var1 + 6
    print(var1)                 # now it prints the changed var1
func2()

print()
# nesting of functions
def shubhu():
    x = 12
    print(x)
    def shubhu1():
        x = 23                  # if we do not declare x here then it show error because above x is not a global
        print(x)                # variable(limited in its function)
    shubhu1()                   # we call shubhu1() here because this function is pvt property of shubhu()
shubhu()
# print(x)                      # this will show error as none of the above x is global.
