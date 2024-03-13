list1=[2,4,5,7]
#print(list(map(addition,list1)))

#filter
def even_n(x):
    if x%2==0:
        return x

print(list(filter(even_n,list1)))