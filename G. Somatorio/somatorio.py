t=int(input())
for i in range(t):
    a=input().split(";")
    b=sum([int(e) for e in a])
    print(b,end="" if i==t-1 else "\n")