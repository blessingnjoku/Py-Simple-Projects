print('welcome to logical quiz game').lower() 


question = raw_input('are you in the mood to play the game? ')
print(question + " !")
the_score =0

if question.lower() !='yes':
    quit()
print('thanks for accepting your first challenge')

quiz_question = raw_input("capital of Nigeria is? ")
if quiz_question.lower()  == "abuja":
    print('correct!')
    the_score +=5
else:
    print('incorrect')

quiz_question = raw_input("is United state of America is a country or continent? ").lower()
if quiz_question == "continent":
    print('correct!')
    the_score +=5
else:
    print('incorrect')

quiz_question = raw_input("who is the haed of the family? ").lower()
if quiz_question == "father":
    print('correct!')
    the_score +=5
else:
    print('incorrect')


quiz_question = raw_input("the fastest animal on land is? ").lower()
if quiz_question == "cheater":
    print('correct!')
    the_score +=5
else:
    print('incorrect')

quiz_question = raw_input("How many sense organ do you have? ").lower()
if quiz_question == "five":
    print('correct!')
    the_score +=5
else:
    print('incorrect')

print('Your total score is ' + str(the_score))
print('you got ' + str((the_score / 5)* 100) + '%.')
