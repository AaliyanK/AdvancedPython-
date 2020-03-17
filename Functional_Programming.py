# Functional programming - packaging of code like OOP - seperate data/functions
# PURE FUNCTION - input a list and function does something to result in a different output
# given the same input, pure functions should always return the same output
# should not produce any side effects - changes in variables, changing things in the outside function

# Useful functions - map/filter/zip/reduce

# MAP - will return the same number of items

my_list = [1,2,3]
def multiply(item):
    return item*2

print(list(map(multiply,[1,2,3]))) # map(input function, data we want the change)
# GREAT replacement for "for loops" - map iterates over the data we input
# map will return item*2 each time - returns a list

# IMPORTANT! map wont change anything from the outside world - pure function
print(list(map(multiply,my_list)))
print(my_list) # will still output [1,2,3]

print(" ")

# FILTER - can return less than what we input

def only_odd(item):
    return item % 2 != 0 # Odd if remainder of two nums is NOT 0 - return odds only

print(list(filter(only_odd,[1,2,3,4,5,6,7]))) # output is filtered and will only return odd!

# ZIP - need two lists/iterables and need to zip them together

list1 = [1,2,3]
list2 = [4,5,6]
print(list(zip(list1,list2))) # GRABS FIRST ITEM IN EACH list then pairs them in a tuple, does the same for the second items
# Can be used in a database where there is a list of names and a list of phone numbers
# we use zip to chain together the entries in the respective order

print(" ")

# REDUCE

def accum(acc,item):
    print(acc,item)
    return acc+item


from functools import reduce
print(reduce(accum,list1,0)) # (function,list,intial) - list is the "item" initial is the "acc"

print(" ")

# EXERCISE

#1 Capitalize all of the pet names and print the list
my_pets = ['sisi', 'bibi', 'titi', 'carla']
def cap(item):
    return item.capitalize()

print(list(map(cap,my_pets)))

#2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5,4,3,2,1]
my_numbers.sort()

print(list(zip(my_strings,my_numbers)))


#3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]

def filt(item):
    return item>50

print(list(filter(filt,scores)))

print(" ")

# LAMBDA Expressions - anonymous functions - use lambda when we only need to use a function once

# lambda argument: action(input)
lamlist = [1,2,3]

print(list(map(lambda item: item*2,lamlist)))
# same thing as: def multiply(item = lamlist):
#     return item*2

print(" ")

# LAMBDA EXERCISE - square a list

square = [5,4,3]

print(list(map(lambda item: item**2,square)))

# List sorting
import operator
a = [(0,2),(4,3),(9,9), (10,-1)]

print(list(map(lambda item: sorted(item),a)))

print(" ")

# LIST COMPREHENSIONS - quick ways of creating dicts/sets/lists

# INSTEAD OF FOR LOOP LIKE:
listcomp = []
for char in 'hello':
    listcomp.append(char)
print(listcomp)

# DO THIS - listcomp = [variable for variable in iterable]

listcomp= [char for char in 'hello']
print(listcomp)

mylist2 = [num for num in range(0,100)] # will just output a list
mylist3 = [num**2 for num in range(0,100)] # [action for variable in range] - will do an action
mylist4 = [num**2 for num in range(0,100) if num%2==0] # add an if statement

print(" ")

# dictionary comprehensions
simpledict = {
    'a':1,
    'b':2
}
my_dict = {key:value**2 for key,value in simpledict.items() if value%2==0} # doing an action on the values if something occurs
print(my_dict)

listdict = {num:num**2 for num in [1,2,3]} # num is the index, we create a dict with key being num and value being num squared

# LIST COMPREHENSIONS EX

some_list = ['a','b','c','b','d','m','n','n']
duplicates = set([item for item in some_list if some_list.count(item)>1]) # USE SET WHEN WE DONT WANT REPITIONS
print(duplicates)