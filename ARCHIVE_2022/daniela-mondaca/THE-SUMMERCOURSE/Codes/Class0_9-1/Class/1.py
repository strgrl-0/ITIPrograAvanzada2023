a=10
b=5

add=a+b
sus=a-b
mult=a*b
div=a/b
divEnfInt=a//b
rest=a%b
exp=a**b


x=str(add)+' '+str(sus)
print(x)
x=str(sus)+' '+str(mult)
print(x)
x=str(divEnfInt)+' '+str(exp)
print(x)

prom=(add+sus+mult+div+divEnfInt+rest+exp)/7
print(prom)