# GENERATORS - generate a sequence of values over time

range(100) # creates them one by one
list(range(100))  # creates a list at once of the range of #s

def make_list(num):
    result = []
    for i in range(num):
        result.append(i*2)
    return result

my_list = make_list(100)
print(my_list) # will use up a lot of memory!

print(list(range(10))) # will use up a lot of memory!

# generators take up LESS space in memory by printing one at a time
# generators are iterable

print(" ")

def generator(num): # MAKING A GENERATOR FUNCTION - python actual way
    for i in range(num):
        yield i # pauses the function and goes back to it when we say so

g = generator(100)
print(next(g)) # will output one at a time!
print(next(g))
print(next(g))

print(" ")

# Generator - Fibbonacci EXERCISE

def fib(num):
    a = 0
    b = 1
    for i in range(num):
        yield a
        temp = a
        a = b
        b = temp + b

for x in fib(20):
    print(x)
print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))


