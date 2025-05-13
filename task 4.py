x = int(input("From: "))
y = int(input("To: "))
if x==y:
    print(x)
else:
    while x<y+1:
        print(x)
        x+=1