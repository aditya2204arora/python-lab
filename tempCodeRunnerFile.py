import functools
import operator
#reduce
sum1=lambda a,b : a+b
list1=[2,4,5,5,6,2,7]
print(functools.reduce(operator.add,list1))