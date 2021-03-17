#N students take K apples and distribute them among each other evenly. The remaining (the undivisible) part remains in the basket. How many apples will each single syudent gets? How many apples will remain in the basket? The program reads the number N and k. It should print the two answers for the questions above.
students = int(input('Enter the number of student'))
apples = int(input('Enter the total number of apples'))
divisible_apples = (apples//students)
remaining_apples = (apples%students)
print(f'each students got {divisible_apples}')
print(f'the remaining apples are {remaining_apples}')
