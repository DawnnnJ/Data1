# -*- coding: utf-8 -*-
# vector add tradition way
def pythonsum(n):
    a=list(range(1,n))
    b=list(range(1,n))
    c=[]
    for i in list(range(len(a))):
        a[i]=i**2
        b[i]=i**3
        c.append(a[i]+b[i])
    return c

#in the numpy way
import numpy as np

def numpysum(n):
    a=np.arange(n)**2  # 生成1-n的数字
    b=np.arange(n)**3
    c=a+b
    return c

#效率对比
import sys
from datetime import datetime

size=1000

start=datetime.now()
c=pythonsum(size)
delta=datetime.now()-start
print(c[-2:])
print(delta.microseconds)

start=datetime.now()
c=numpysum(size)
delta=datetime.now()-start
print(c[-2:])
print(delta.microseconds)

#NUNMPY
x=np.arange(5)
z=x.dtype #数据类型
y=x.shape #数组长度

print(x)
print(str(y))
print(z)

#创建多维数组
m = np.array([np.arange(2), np.arange(2)])#2*2 arrays
print(m)

print(m.shape)
print(m.dtype)











