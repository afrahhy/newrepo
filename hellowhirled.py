input('Anyone there?')
print('hello werld')
answer = input('did I spell that right?' )
answer = answer.lower()

# def understandanswer(answer):
#     if answer == 'yes' or 'yeah' or 'yh' or 'yea' or 'no':
#         return True
#     else:
#         return False

# print(understandanswer(answer))

if answer != 'yes' or 'no':
    answer = input("I didn't understand, could you repeat that?")

if answer == 'yes':
    print('Okay, thanks')
elif answer == 'no':
        print('sorry, i meant to say "hello world"')
else:
    print("oops")
