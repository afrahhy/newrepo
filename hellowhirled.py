input('Anyone there?')
print('hello whirled')
answer = input('did I spell that right?' )
answer = answer.lower()

if not bool(answer=='yes') or not bool(answer=='no'):
    answer = input("I didn't understand, could you repeat that?")

if answer == 'yes':
    print('Okay, thanks')
if answer == 'no':
        print('sorry, i meant to say "hello world"')
# else:
#     print("I didn't understand, can you repeat that?")
#     answer = input
