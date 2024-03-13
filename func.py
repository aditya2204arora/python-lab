

#function args #optional
def addition(n1,n2=6):
    return n1+n2

num1=int(input())
num2=int(input())
print(addition(num1,num2))

print(addition(num1))

#noormal func
def myname():
    return "Hello"

name=input("your name: ")
print(myname() + " " + name)

#multiple args
def multipleargs(*names):
    for name in names:
        print(f"Hello {name}")

multipleargs('adi','jacob','peter')

#lambda

sum=lambda a,b,c : a+b+c
print(sum(4,6,4))


max=lambda a,b: a if a>b else b
print(max(5,2))

#map func
list1=[2,4,5,7]
print(list(map(addition,list1)))

#filter
def even_n(x):
    if x%2==0:
        return x

print(list(filter(even_n,list1)))


import functools
import operator
#reduce
sum1=lambda a,b : a+b
list1=[2,4,5,5,6,2,7]
print(functools.reduce(operator.add,list1))


