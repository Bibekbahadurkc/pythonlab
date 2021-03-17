#Game finding a secret number within 3 attempts using while loop.
t = 0
while t<3:
    Secret_number = int(input('guess:'))
    if Secret_number == 50:
        print('you won')
        break
    else:
        print('wrong')
    t +=1
else:
    print('sry your attempt has been completed')
