# num=int(input("enter the number:"))
# if num in range(91,100):
#     print("super smart")
# elif num in range(81,90):
#     print("smart")
# elif num in range(71,80):
#     print("smart enough")
# elif num in range(61, 70):
#     print(" just smart ")
# elif num in range(36, 60):
#     print(" no smart ")
# elif num in range(0,35):
#     print(" dumb ")
# elif num in range(0,100):
#     print("number is in range")
# else:
#     print("invalid input")

# sum=0
# for i in range(56,153):
#     sum=sum+1
# print(sum)

# str=("CVCORP")
# for i in range(33):
#     print(str)

# for i in range(700,900):
#     if i % 2 == 0:
#         print(i)

# for i in range(250,550):
#     if i%11==0:
#         print(i)

# a=10
# b=200
# c=30
# if (a>b):
#     if (a>c):
#         print("a is big")
#     else:
#         print("b is big")
# else:
#     if (b>c):
#         print("b is big")
#     else:
#         print("c is big")
#
# print(("CVCORP\n")*33)

# a=15300# if a  not in range(100,1000):
#     print("wrong number")
# else:
#     if a %2==0:
#         print("even")
#     else:
#         print("odd")

# l=[1,7,8,12,14,21,22,66]
# k=list(map(lambda x:x**3,l))
# filter(lambda x:x%4==0 ,k)
# print(k)
#
from functools import reduce
# l=[1,2,3,4,5,6,7,8,9,10]
# reduce(lambda x,y: x+y,l)
#

# from functools import reduce
# l=[1,7,6,3,8,9,11,10]
# k=reduce(lambda x,y:x if x>y else y,l)
# print(k)
#
# l=[0,22,31,35,23]
# # convertin in to celisus to forieng heat formula# F=((9/5)*C)+32
# F=(list(map(lambda(9/5*x)+32,l)))
# fi=list(filter(lambda x:x%3==0,&))

# kg=5.6
# grams = kg*1000
# print(grams)

# c=80
# f=(c*9/5)+32
# print(f)


# sorted
# # syntax: sorted(l,key=lambda x: x%3==0)
# l=[23,21,27,28,44,46]
# k=sorted(l, key=lambda x:x%7,reverse=True)
# print(k)
#
# l=[23,21,27,28,44,46]
# k=sorted(l, key=lambda x:x%7)
# print(k)

# maps  -- used to aplly a fun to every element in a sequence
# numbers=[1,2,3]
# k=list(map(lambda x:x*2,numbers))
# print(k)

# a=[1,2,3,4]
# b=[10,20,30,40]
# k=list(map(lambda x,y:x+y,a,b))
# print(k)

# 2
# a=[1,2,3]
# b=[10,20,30,40]
# k=list(map(lambda x,y:x+y,a,b))
# print(k)

# nums=[1,2,3,4]
# k=list(filter(lambda x: x%2==0,nums))
# print(k)

# 3
# nums=[12,15,7,18,20,21,25]
# k=list(filter(lambda x: (x%3==0 or x%5==0)and not (x%3==0 and x%5==0),nums))
# print(k)

# 4
# from functools import reduce
# nums=[1,2,3,4]
# k=reduce(lambda x,y:x+y,nums,10)
# print(k)

# friday

# nums=[[1,2],[3,4],[5,6]]
# k=list(map(lambda x:x+[5],nums))
# print(k)
#
# d={"apple":100,"banana":40,"cherry":150}
# # k=list(filter(lambda item:item[1]>50,d.items()))
# print(k)

# from functools import reduce
# num=[12,13,15,26,56,78,86,90]
# k=reduce(lambda x,y:x if x>y else y,num)
# print(k)

# num="kavya"
# k=list(map(ord, num))
# print(k)

# num="kavya naga gorantla"
# vowels="aeiouAEIOU"
# k=list(filter(lambda x:x not in vowels,num))
# print(k)

# import functools
# num=['k', 'v', 'y', 'n', 'g', 'g', 'r', 'n', 't', 'l']
# k=reduce(lambda x,y:x+y,num)
# print(k)git

# num=[10,350,10,350,20]
# k=list(map(id, num))
# print(k)
import functools
# num=[10,15,20,25,30]
# k=reduce(lambda x,y:x+y,filter(lambda x: x%5==0,map(lambda x:x**2,num)))
# print(k)