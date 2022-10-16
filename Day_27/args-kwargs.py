## Example 1
## Use **kwargs as myFun Function argument
def myFun(**kwargs):
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))

# Driver code
myFun(first='Geeks', mid='for', last='Geeks')


## Example 2
## Use **kwargs as input to myFun Function
def myFun(arg1, arg2, arg3):
    print("arg1:", arg1)
    print("arg2:", arg2)
    print("arg3:", arg3)

# Now we can use *args or **kwargs to
# pass arguments to this function :
args = ("Geeks", "for", "Geeks")
myFun(*args)

kwargs = {"arg1": "Geeks", "arg2": "for", "arg3": "Geeks"}
myFun(**kwargs)


## Example 3
## Use *args, **kwargs as myFun Function argument
## Will filter them automatically
def myFun(*args, **kwargs):
    print("args: ", args)
    print("kwargs: ", kwargs)

# Now we can use both *args ,**kwargs
# to pass arguments to this function :
myFun('geeks', 'for', 'geeks', first="Geeks", mid="for", last="Geeks")


## Example 3
## Using *args and **kwargs to set values of object (class)

# Using *args
class car():  # defining car class
    def __init__(self, *args):  # args receives unlimited no. of arguments as an array
        self.speed = args[0]  # access args index like array does
        self.color = args[1]

# creating objects of car class
audi = car(200, 'red', 'nofail') # 'nofail' won't be obtained
bmw = car(250, 'black')
mb = car(190, 'white')

print(audi.color)
print(bmw.speed)

# Using *k*wargs
class car():  # defining car class
    def __init__(self, **kwargs):  # args receives unlimited no. of arguments as an array
        self.speed = kwargs['s']  # access args index like array does
        self.color = kwargs['c']

# creating objects of car class
audi = car(s=200, c='red', nofail='sd')  # nofail key won't be obtained
bmw = car(s=250, c='black')
mb = car(s=190, c='white')

print(audi.color)
print(bmw.speed)
