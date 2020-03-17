# OOP

print(type('hi'))  # will output a class type - str


# MAKING OUR OWN CLASS/OBJECT

class BigObject:  # the blueprint of what we want to create - attributes of our class
    pass


obj1 = BigObject()  # Create objects/INSTANCES with the blueprint - called instanciating
obj2 = BigObject()
obj3 = BigObject()

print(type(obj1))


# MAIN IDEAS
class PlayerCharacter:  # Naming convention: singular and no underscores
    membership = True  # Class Object Attribute - it is STATIC - cannot be changed - will be the same for all objects

    def __init__(self, name='bob', age=1):  # can assign default parameters
        if self.membership:  # run the PlayerCharacter class only if membership is TRUE
            self.name = name
            self.age = age

    def shout(self):  # this is a method so we need .shout()
        print(f"My name is {self.name}")  # ALWAYS NEED self.name/age when in the class
        return 'bumba'  # this wont produce a "None" when you run it

    @classmethod  # dont need to instantiate when using "class methods"
    def adding_things(cls, num1, num2):
        return cls('teddy', num1 + num2)  # USE CLASSMETHOD WHEN WE WANT TO USE PARAMETERS FROM THE CLASS

    @staticmethod  # USE WHen we dont need class parameters
    def adding_things2(num1, num2):
        return num1 + num2


player1 = PlayerCharacter('bumba', 44)  # pass in the name into the class
player2 = PlayerCharacter('Tom', 21)  # pass in properties to the class so that they can be called with .name/.age
player2.attack = 50  # we can now create attributes on the go like this

print(player1.name)  # outputs "bumba"
print(player2.name)  # outputs "Tom"

print(player1.age)
print(player2.age)

print(player1.shout())

print(player2.attack)  # will output 50

print(player1.membership)  # will output true because we set it as true in the class

print(player1.adding_things(1, 3))
print(PlayerCharacter.adding_things(2, 40))  # NO NEED TO INSTANTIATE, JUST CALL THE METHOD

# CATS EXERCISE
print(" ")
print(" ")


# Given the below class:
class Cat:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats
cat1 = Cat('gary', 1)
cat2 = Cat('boom', 2)
cat3 = Cat('liz', 3)
print(cat2.name)

age_list = [cat1.age, cat2.age, cat3.age]
print(age_list)


# 2 Create a function that finds the oldest cat
def age(list_age):
    for x in list_age:
        return max(list_age)


print(age(age_list))

answer = age(age_list)
print(answer)


# OR:
def oldest_cat(*args):
    return max(args)


# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
print(f"The oldest cat is {answer} years old")

# OR:

print(f"the oldest cat is {oldest_cat(cat1.age, cat2.age, cat3.age)} years old")
# directly calls function with ARGS within the string

print(" ")
print(" ")


# 4 PILLARS OF OOP

# ENCAPSULATION - the binding of data into one object

def run():  # this is a method so we need .shout()
    print('run')


class Encapsulation:  # Naming convention: singular and no underscores
    membership = True  # Class Object Attribute - it is STATIC - cannot be changed - will be the same for all objects

    def __init__(self, name='bob', age=1):  # can assign default parameters
        if self.membership:  # run the PlayerCharacter class only if membership is TRUE
            self._name = name  # the convention - _name is used for private variables
            self._age = age

    def speak(self):
        print(f'My name is {self._name} and I am {self._age} years old')


Encap1 = Encapsulation('Aaliyan', 50)
Encap1.speak()

print(" ")
print(" ")

# SECOND PILLAR - ABSTRACTION - Hiding info and providing access to important information only
# Encap1.speak()  # we dont see what is going on behind the scenes
# Encap1.speak = 'booo' - this will change the function in the class - we DONT want this
# use private variables so that this change does not occur - use _name/_age

print(" ")


# THIRD PILLAR - INHERITANCE - allows new object to take on properties of existing objects

# users can be wizards/archers - need to be signed in first

class User():  # main class that we will be using in other classes
    def __init__(self, email):
        self.email = email

    def sign_in(self):
        print("logged in")

    def attack(self):  # WILL POLY this with WIZARD
        print("do nothing")


class Wizard(User):  # pass in the main class that is to be inherited
    def __init__(self, name, power, email):  # enter 3 parameters when instanciating
        super().__init__(email)  # super refers to the class above (USER) - TAKING EMAIL argument FROM USER CLASS
        self.name = name
        self.power = power

    def attack(self):
        User.attack(self)  # This accepts the poly from USER
        print(f"attacking with power of {self.power}")


class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f"attacking with arrows: arrows left -  {self.num_arrows}")


wizard1 = Wizard('Merline', 50, 'bumba@gmail.com')  # INSTANCES
archer1 = Archer('robin', 500)

print(wizard1.sign_in())  # we inherited from the USER class
print(wizard1.attack())

print(archer1.attack())  # attack is different for the wizard and archer classes
print(archer1.sign_in())  # INHERITED!

# isinstance(instance, class) # give it the instance then the class
print(isinstance(wizard1, Wizard))  # will return True/False if the wizard1 is an instance of Wizard
print(isinstance(wizard1, User))  # will return True because Wizard class is in User class

print(" ")

# FOURTH PILLAR - POLYMORPHISM - object classes sharing the same method names
# consider the attack names in the above code, archer and wizard objects output different things
# what if we want USER and WIZARD to output the same "ATTACK" output

print(wizard1.attack())  # will output "DO NOTHING" and "attacking with power of 50"

# LEARNING SUPER()
print(wizard1.email)  # will work because we used super in the code above

# INTROSPECTION
print(dir(wizard1))  # use when we want to find out what we have access too - lots of dunder methods will be output

print(" ")


# OOP EXERCISE

class Pets():
    animals = []

    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())


class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'


class Simon(Cat):
    def sing(self, sounds):
        return f'{sounds}'


class Sally(Cat):
    def sing(self, sounds):
        return f'{sounds}'


# 1 Add another Cat
class bob(Cat):
    def sing(self, sounds):
        return f'{sounds}'


# 2 Create a list of all of the pets (create 3 cat instances from the above)
Bob = bob('bob', 10)
Simon = Simon('Simon', 20)
Sally = Sally('Sally', 30)
my_cats = [Bob, Simon, Sally]

# 3 Instantiate the Pet class with all your cats use variable my_pets
my_pets = Pets(my_cats)

# 4 Output all of the cats walking using the my_pets instance
my_pets.walk()

print(" ")


# DUNDER METHODS
class Toy():
    def __init__(self, color, age):
        self.color = color
        self.age = age
        self.my_dict = {  # used for __getitem__
            'name': 'yoyo',
            'has_pets': False
        }

    def __str__(self):  # MODIFYING THE DUNDER METHOD!
        return f'{self.color}'  # __str__ will return "red" now

    def __call__(self):  # will let us call action_figure() with brackets
        return ("yessss")

    def __getitem__(self, i):  # "i" is the index
        return self.my_dict[i]


action_figure = Toy('red', 0)
print(action_figure.__str__())  # will return red because we changed it
print(str(action_figure))  # same thing as above
print(action_figure['name'])  # call the dictionary defined in the "toy" class

print(" ")


# DUNDER METHODS - LIST EX

class SuperList(list): # TO AQUIRE THE POWERS OF LIST - ALL ITS DUNDER METHODS, USE INHERITANCE!!
    def __len__(self, mylist):
        return 1000 # editing the actual len METHOD to return 1000 instead of len


gang = [1,2,3,4]
super_list1 = SuperList()

print((super_list1.__len__(gang))) # will always return 1000 because we changed it
super_list1.append(5) # it has list powers so we can use append

print(super_list1[0])
print(issubclass(SuperList,list)) # is superlist a subclass of list?? returns true/false

print(" ")

# MULTIPLE INHERITANCE - very complex, we shouldnt use this

class Gang():
    def sign_in(self):
        print('logged in')

class robber(User):
    def __init__(self,name,power):
        self.name = name
        self.power= power

    def attack(self):
        print(f'attacking with power of {self.power}')

class cop(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def check_arrows(self):
        print(f"attacking with arrows: arrows left -  {self.num_arrows}")

    def run(self):
        print('ran really fast')

class hybrid(robber,cop): # will have cop and robber powers - MULTIPLE INHERITANCE
    def __init__(self,name,power,arrows): # need to make sure we cover ALL the parameters in the other classes
        cop.__init__(self,name,arrows) #
        robber.__init__(self,name,power)


hb = hybrid('bryan',20,30) # we can now enter the multiple inherited class parameters
print(hb.run()) # this is a cop class
print(hb.check_arrows()) # this is from the robber class

print(hb.attack())

print(" ")

# METHOD RESOLUTION ORDER - "FIRST IN LINE"

class A:
    num = 10

class B(A):
    pass

class C(A):
    num = 1

class D(B,C):
    pass

#       A
#    /      \
#   /         \
#  B           C
#  \          /
#     \   /
#        D

print(D.num) # will output "1" because it reaches C = 1 before it reaches A
print(D.mro()) # will give us the order that it checks the classes in