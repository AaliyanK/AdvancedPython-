# Modules are a way of organizing code
# How do you import functions from other files?

from for_module import mult,divide # pycache will be created everytime you link two python files

from Shopping.more_shopping.Shopping_cart import buy

if __name__ == '__main__': # USE TO ONLY RUN CODE FROM MAIN FILE


    # print(for_module) # will output file path
    # print(for_module.divide(2,3)) # Calling functions from other python file!
    # CLEANER:
    print(divide(5,3))
    print(mult(2,3))

    # print(more_shopping.Shopping_cart)
    # print(more_shopping.Shopping_cart.buy('apple'))
    print(buy('gang'))

    print(__name__)
    print('please run this')