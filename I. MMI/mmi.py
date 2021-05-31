t=int(input())
for i in range(t):
    a=input().split(" ")
    b=int(a[0])
    c=int(a[0])
    for e in range(len(a)):
        if int(b) > int(a[e]):
            b=a[e]
    for e in range(len(a)):
        if int(c)<int(a[e]):
            c=a[e]
    print(str(b)+" "+str(c))
    print("S" if b==c else "N",end="" if i==t-1 else "\n")