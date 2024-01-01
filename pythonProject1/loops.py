#for loop in python

for i in range(1,10):
    print(i)

#for loop using list
list = ["hiba", "maeve", "david", "simon", "fariha"]
for item in list:
    print(item)

#for loop using set
set = {7,99,35,938,39}
for item in set:
    print(item)

#while loop
i=1
while(i < 9):
    print(i)
    i += 1


#infinite while loop
'''while(True):
    print("hiba")'''

#Also infite loop but have added 'break' keyword to exit loop
while(True):
    num = int(input("Enter any number: "))
    print(num)
    if(num == 0):
        break

print("program has finished executing..")


