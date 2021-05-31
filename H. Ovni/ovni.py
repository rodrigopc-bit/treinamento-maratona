t=int(input())
for i in range(t):
    a=input().split(" ")
    b=int(a[0])+int(a[1])
    if b>int(a[2]):
        print("NAO CABE!",end="" if i==t-1 else "\n")
    else:
        print("CABE!",end="" if i==t-1 else "\n")