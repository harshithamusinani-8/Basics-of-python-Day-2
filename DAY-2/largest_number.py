a=int(input("enter a:"))
b=int(input("enter b:"))
c=int(input("enter c:"))
if (a==0 & b==0 & c==0):
    print("all are zeros")
else:
    if(a>b&a>c):
        print(a,'is largest number')
    elif(b>c):
        print(b,'is largest number')
    else:
        print(c,'is largest number')


