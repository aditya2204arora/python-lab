# def even():
#     evnlist=[]
#     for i in range(20):
#         if i%2==0:
#             evnlist.append(i)
#     return evnlist

# print(even())

def even():
    for i in range(20):
        if i%2==0:
            return i

for i in even():
    print(i)