acceptablewords = ['yes','yeah', 'yh', 'yea', 'no', 'nay', 'nah']
input('Anyone there?')
print('hello werld')
print('...')
answer = input('did I spell that right?' )
answer = answer.lower()

if answer not in acceptablewords:
    answer = input("I didn't understand, could you repeat that?")

if answer == 'yes':
    print('Okay, thanks')
elif answer == 'no':
        print('sorry, i meant to say "hello world"')
else:
    print("oops")
