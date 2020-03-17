import random # as "nickname"

print(random)

# help(random) to understand the module

print(random.random())
print(random.choice([1,2,3,4,5]))
print(random.randint(1,10))

mylist = [1,2,3,4,5]
random.shuffle(mylist)
print(mylist)