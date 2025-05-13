a = int(input("First num: "))
b = int(input("Second num: "))
c = input("Task: ")
if c=="+" :
    print(a+b)
if c=="-" :
    print(a-b)
if c=="*" :
    print(a*b)
if c=="/" :
    if b==0:
        print("division by zero")

    else:
        print(a/b)