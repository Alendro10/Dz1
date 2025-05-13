from random import *
num = randint(1,10)

for i in range(3) :
    user_num = int(input("guess the number: "))
    if user_num > num:
        print("the number smaller")
    elif user_num < num:
        print("the number bigger")
    else:
        print("You guessed!")
print("Guessed number is "+str(num))