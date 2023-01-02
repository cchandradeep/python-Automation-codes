print("hai this is chandradeep reddy")
# name of the employee -single line comment
"""
hfhf 
 fjf
 ff -multi-line comment

"""
# what is a data type?
# Data types are the classification or categorization of data item
"""
int, Boolean, float,

variable is defined as A variable is a container for a value. It can be assigned a name, you can use it to refer to it later in the program. Based on the value assigned, the interpreter decides its data type. You can always store a different type in a variable. For example, if you store 7 in a variable, later, you can store 'Dinosaur'.


"""
a=True
print(type(a))
b=4
print(type(b))
c=2020.09
print(type(c))
'''
Define the local and Global variables with the same name and print both variables and understand the scope of the variables?
`Global variables are declared outside the functions whereas local variables are declared within the functions.

'''
e=10
def func():
    global e
    e+=10
    print("Value inside the function:",e)
func()
print("Value Outside the function:",e)

def fun():
    a = 10
    print('local variable',a)

fun()

