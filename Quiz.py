## * User interacting projects
## * Project presentation


print('Welcome to movie Quiz')
answer = input('Are you ready to play the Quiz ? (yes/no) :')
score = 0
total_questions = 3

if answer.lower() == 'yes':
    answer = input('Question 1: What role made Travis Fimmel famous?')
    if answer.lower() == 'vikings':
        score += 1
        print('correct')
    else:
        print('wrong Answer :(')

    answer = input('Question 2: Can vikings online to be seen? ')
    if answer.lower() == 'yes':
        score += 1
        print('correct')
    else:
        print('Wrong Answer :(')

    answer = input('Question 3: What is the name of Finland Capital ?')
    if answer.lower() == 'helsinki':
        score += 1
        print('correct')
    else:
        print('Wrong Answer :(')

print('Thankyou for Playing this small quiz game, you attempted', score, "questions correctly!")
print('your score is ', score)


