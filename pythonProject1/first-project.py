'''
print("fuck world!")

#variables in pyhton (every var is obj in python)
a = 3 #int
print(a)
b = 10
print(b)
a = 4.4 #float
print(a)
c = "Hiba"
print(c) #string
d = True #boolean
print(d)
e = None #none type var
print(e)

#typecasting (covert 1 datatype to another)
x = "5"
print(int(x)+1) #convert 'x' into 'int' to concatenate with '1'

y=5
print(y+1)
'''

#types of operators

#arithmatic operators
num1 = 10
num2 = 5

print("num1 + num2",num1 + num2)
print("num1 - num2",num1 - num2)
print("num1 * num2",num1 * num2)
print("num1 / num2",num1 / num2)
print("num1 // num2",num1 // num2) #float no's division
print("num1 ** num2",num1 ** num2) #exponential operator
print("num1 % num2",num1 % num2) #modulus

#assignment operators

a = 4  #4 is assigned to a
print(a)

a += 4
print("sum:",a)

a -= 4
print("subtraction:",a)

a *= 4
print("multiplication:",a)

a /= 4
print("division:",a)

a //= 4
print("float division:",a)

a **= 4
print("exponent:",a)

a %= 4
print("modulus:",a)

#comparison operators
x = 5
y = 10
z = 15

print(x>y) #'x' is greater than '5'
print(x<y)
print(x==y) #'x' and 'y' should've same values
print(x!=y)
print(x<=y) #'x' is less than or equals to 'y'
print(x>=y)

#logical operators
print(x>y and x==z)
print(x<y or x==z)
print(not(True)) #not --> reverse true var