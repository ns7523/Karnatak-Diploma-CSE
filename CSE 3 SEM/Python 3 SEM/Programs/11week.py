import numpy as n
a1=n.array([[1,2],[5,6]])
a2=n.array([[8,9],[1,2]])
print("array add : \n",a1+a2)
print("array sub : ",a1-a2)
print("array multi : ",a1*a2)
print("array div : ",a1/a2)
print("power of arrays : ",pow(a1,a2))
print("min in a1 :",n.min(a1))
print("max in a1:",n.max(a1,axis=1))
print("mean of a1 :",n.mean(a1))
print("median of a1:",n.median(a1))
