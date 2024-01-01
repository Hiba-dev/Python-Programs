#Try and Except (Exception handling in python)

try:
    x = int(input("Enter anything: "))
    print(x + 5)

except Exception as e:
    print("some error occured", e)