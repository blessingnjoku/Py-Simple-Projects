import random

print('Hello my friend, here is the ')
question = raw_input('are you good at guessing? ')
if question == 'yes':
    print("lets find out")



user_value = raw_input('Type a number ')

# check if the the value is a number
if user_value.isdigit():

    # convert to integers
    user_value =int(user_value)
    if user_value <=0:
        print('0 is the forbidden number ')
        quit()
else:
    print('only numbers are recognize ')

random_value = random.randint(0, user_value)

total_correct_guesses =0

while True:
    total_correct_guesses += 1
    user_guess = raw_input('Make a guess: ')

    if user_guess.isdigit():
       user_guess = int(user_guess)
    else:
        print('only numbers are recognized')
        continue
    if user_guess == random_value:
        print('yepp!, you got it')
        break
    elif user_guess > random_value:
           print('you guessed above the number')
    else:
        print('you guessed below the number ')
        
print('you guessed',  total_correct_guesses, 'correctly ')


  