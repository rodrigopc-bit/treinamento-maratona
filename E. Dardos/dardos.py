x, y = map(int, input().split())
if(x>0 and x<=50):
    if(y>0 and y<=50):
        print("R1",end="")
    if(y<0 and y>=-50):
        print("R4",end="")
if(x<0 and x>=-50):
    if(y>0 and y<=50):
        print("R2",end="")
    if(y<0 and y>=-50):
        print("R3",end="")
if(x==0 and y==0):
    print("NO ALVO!",end="")