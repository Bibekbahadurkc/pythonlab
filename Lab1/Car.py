#Build the car game: Car game
caar = False
car = True
while car:
    ans = input(':').lower()
    if ans == "help":
        print('''start = to start the car
stop = to stop the car
quit = to quit the car''')
    elif ans == "start":
        if caar:
            print('the car has already started')
        else:
            print('the car has started')
            caar = True
    elif ans == 'stop':
        if caar:
            print('the car has stopped')
            caar = False
        else:
            print('the car has already stopped')
    elif ans == 'quit':
        break
    else:
        print('''please enter correctly... type 'help' for help''')