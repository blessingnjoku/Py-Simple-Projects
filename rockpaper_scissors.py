import random



computer_score=0
player=0

name_options = ['rock', 'paper', 'scissors']

while True:
    user_input=raw_input('Type Rock/Paper/Scissors or type q to quit ').lower()
    if user_input == 'q':
        break

    if user_input not in name_options:
       continue

    # generate random number
    random_num = random.randint(0,2)
    computer_picked = name_options[random_num]
    print('computer picked', computer_picked + '.')

    if user_input == 'rock' and computer_picked == 'scissors':
        print('you got it!')
        player += 2
       

    elif user_input == 'paper' and computer_picked == 'rock':
         print('you got it!')
         player += 2
        

    elif user_input == 'scissors' and computer_picked == 'paper':
        print('you got it!')
        player += 2
    else:
        print('ah! fail')
        print('play again')
        computer_score+=1
      
print('you scored', player)
print('computer scored', computer_score)

print('Goodbye!')