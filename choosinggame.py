my_name = raw_input('type your name ')
print(my_name)

resp= raw_input('you are at the end of a road and u need to choose to go right or left ').lower()

if resp == "left":
  resp = raw_input('you are at the sea, you can "swim " or "use a boat" ')

  if resp == 'swim':
    print('you swan and played with the shakes')

  elif resp == 'use a boat':
    print('you enjoyed the waves')

  else: 
       print('invalid choice you lose')
       
elif resp == 'right':
    print('you have found a library of book')
    print('do you want to "read" to "go back" ')

    if resp == 'read':
        resp = raw_input('we have two books for u. choose "tommy" or "johnny" ')
        if resp == 'tommy':
           print('i hope you love the book')
        elif resp == 'johnny':
            print('johnny must be boring')
    elif resp == 'back':
        print('you ended your adventure')




else:
    print('invalid choice you lose')
