'''
num = int(input("Enter any number: "))

if (num > 10):
    print(f"number is {num}")

elif (num == 10):
    print(f"number is {num}")

else:
    print("bye!!")
'''
from unittest import case

num = int(input("Enter any number: "))

match num:
    case 1_10:
        print(f"Table of {num} is: ")
for i in range (1,11):
 print(f"{num} x {i} = {num * i}")


