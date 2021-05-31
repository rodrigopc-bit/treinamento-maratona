x = input().split(" ")
a = float(x[0])
b = float(x[1])
c = float(x[2])
ab = (a+b+abs(a-b))//2
abc = (c+ab+abs(ab-c))//2
print(int(abc),end='')