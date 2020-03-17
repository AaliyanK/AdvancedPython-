# decorators - supercharges our functions and adds more functionality

# Higher Order Functions: function that accepts another function as a parameter
def greet(func):
    func()

# Also a function that returns another function is  HOF
def greet2():
    def func():
        return 5
    return func

# DECORATORS - basically external tools we can use to add to functions

def my_decorator(func): # THIS SYNTAX IS FOR DECORATORS
    def wrap_func(*args, **kwargs): # this will print the stars around the function
        print('*******') # the actions the decorator will do
        func(*args, **kwargs) # this is the hello()/bye() function
        print('*******')
    return wrap_func

@my_decorator # must be the same name as the function itself
def hello(): # WILL NOT WORK IF THERE ARE PARAMETERS
    print('yeo')

@my_decorator
def bye():
    print('cya')

# Decorators with parameters: make sure you make changes to the DECORATOR FUNCTION AS WELL
# USE ARGS/KWARGS
@my_decorator
def decfunc(greeting, emoji=':)'):
    print(greeting)
    print(emoji)

decfunc('what is UP')

print(" ")

# PERFORMANCE DECORATOR EX
from time import time

def performance(func):
    def wrapper(*args,**kwargs):
        t1 = time() # a stamp for when the func starts running
        result = func(*args,**kwargs) # THIS IS THE FUNCTION
        t2 = time() # a stamp for when the func ends
        print(f'took {t2-t1} seconds')
        return result
    return wrapper

@performance
def long_time(): # we want to see how long it takes to complete this function
    for i in range(1000000):
        i*5

long_time()

print(" ")
# EXERCISE

# Create an @authenticated decorator that only allows the function to run is user1 has 'valid' set to True:
user1 = {
    'name': 'Sorna',
    'valid': True #changing this will either run or not run the message_friends function.
}

def authenticated(fn):
    def wrapper(user):
        print(user['valid'])
        if user['valid'] == True:
            fn(user)
        else:
            print('nah b')

    return wrapper

@authenticated
def message_friends(user):
    print('message has been sent')

message_friends(user1)

