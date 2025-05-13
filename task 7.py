mark = int(input("Your mark is "))
if mark<0 or mark>100 :
    print("not real result")
elif mark<50:
    print("bad")
elif mark<70:
    print("not bad")
elif mark>90:
    print("good")
else:
    print("excellent")