#Write a Python program to convert seconds to day, hour, minutes and seconds.
second = int(input("Enter the value of second: "))
day = (((second//60)//60)//24)
print(f"Total day for given seconds: {day}")

hour = ((second//60)//60)
print(f"Total hours for given seconds: {hour}")

minutes = (second//60)
print(f"Total minutes for given seconds: {minutes}")