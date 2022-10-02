import random


user_value = raw_input('guess a number')

# check if the the value is a number

if user_value.isdigit():
    # convert to integers
    user_value =int(user_value)
