a=int(input())
b = a//100
c = (a - b*100)//50
d = (a - b*100 - c*50)//20
e = (a - b*100 - c*50 - d*20)//10
f = (a - b*100 - c*50 - d*20 - e*10)//5
g = (a - b*100 - c*50 - d*20 - e*10 - f*5)//2
h = (a - b*100 - c*50 - d*20 - e*10 - f*5 - g*2)//1


print(b,"nota(s) de R$ 100")
print(c,"nota(s) de R$ 50")
print(d,"nota(s) de R$ 20")
print(e,"nota(s) de R$ 10")
print(f,"nota(s) de R$ 5")
print(g,"nota(s) de R$ 2")
print(h,"nota(s) de R$ 1",end='')