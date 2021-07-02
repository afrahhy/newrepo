input('Anyone there?')
print('hello whirled')
answer = input('did I spell that right?' )
answer = answer.lower()

if answer != 'yes' or 'no':
    answer = input("I didn't understand, could you repeat that?")

if answer == 'yes':
    print('Okay, thanks')
elif answer == 'no':
        print('sorry, i meant to say "hello world"')
else:
    print("oops")
