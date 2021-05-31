import operator
allowed_operators={
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.floordiv}
a=int(input())
b=input()
c=int(input())
d=input()
e=int(input())
if(a,b,c>=-5 and a,b,c<=5):
    if not((b=="/" and c==0) or (d=="/" and e==0)):
        if(d=="/" or d=="*"):
            f=allowed_operators[d](c,e)
            g=allowed_operators[b](a,f)
            print(g,end="")
        else:
            f=allowed_operators[b](a,c)
            g=allowed_operators[d](f,e)
            print(g,end="")
    else:
        print("erro",end="")