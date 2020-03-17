# ERROR HANDLING

# print(1+'hello') # this error is called an exception

while True:
    try:
        age = int(input("what is your age? ")) # put int so age will always be a number
        print(age)
        10/age
    except ValueError: # if anything errors out, do this: check out documentation to specify ur error type
        print('Please enter a number')
        continue
    except ZeroDivisionError:
        print('Enter value higher than 0')
        break
    else: # if there is no error, do this
        print('thank you')
        break # leave the while loop
    finally: # no matter what this code will output - could be used to log something!
        print('okay im finally done!')

print(" ")

def sum(num1,num2):
    try:
        return num1+num2
    except (TypeError, ZeroDivisionError) as var: # as var allows the error to output a description of an error
        print(f'Please Enter numbers {var}') # can also handle multiple errors!

print(sum('1',2))
