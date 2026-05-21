from pkg_resources import null_ns_handler


# # print("hello kavya")


# a=10
# b=20
# print(a//b)
# print(a*b)
# print(a/b)
# print(a%b)

# name="kavya"
# surname="gorantla"
# print(name+surname)

# wishlist='''i would like to tell about whishlist things to do, my whishlist things are i want to go outside at nyt time and njoy the nyt tym view in hyd'''
# print(wishlist)




# num=int(input("enter the number:"))
# if num % 2==0:
#     print("even")
# else:
#     print("odd")

# a=20
# b=30
# c=40
# if (a>b):
#     if (a>c):
#         print("a is big")
#     else:
#         print("c is big")
# else:
#     if (b>c):
#         print(" b is big")
#     else:
#         print("c is big")



# num=int(input("enter the number:"))
# if num > 0:
#     print("postive")
# elif num < 0:
#     print("negative")
# else:
#     print("zero")

# a=int(input("enter the a:"))
# b=int(input("enter the b:"))
# temp = a
# a=b
# b=temp
# print(a)
# print(b)

# num=int(input("enter the number:"))
# for i in range












# print("my age:" + str("21"))
# print(123 + 456)
# print(2-1)
# print(8*6)
# print(6/4)
# print(3* 3 + 3 / 3- 3)

# bmi calculater
# height=1.65
# weight=5
# bmi=5/1.65**2
# print(bmi)
# print(round(bmi))
# print(round(bmi,2))

# print(6 + 4 / 2 -(1*2))

# tip calculater
# print("welcome to the Tip Calculater!")
# input("what was the total


# x=y=z="kavya"
# print(x)
# x,y,z= " my" , "name" ,"kavya"
# print(x,y,z)


# arbitary parameters
# positional arguments (*)
# def fun(*a):
#     print(a)
#     print(*a)
# fun(10,10,30,40,60)
# *a means positional arguments in arbitary arguments it can pass any number of arguments by using the * symbol
# it converts into tuple format it gives output in tuple format
# print(*a) means unpacking the arguments


# keyword arguments
# def fun3(a,b,c,d):
#     print(a,b,c,d)
# def fun2(**b):
#     print(b)
#     print(**b)
# fun3(a=75,b=30,c=40,d=70)

# def fun3(a,b,c,d):
#     print(a,b,c,d)
# fun3(a=75,b=30,c=40,d=70)

# def fun5(*a,*b):
#     print(a,b,sepz"\n")
# fun5(10,1,7,3,8,6,7,10)

# def fun5(*a,**b):
#     print(a,b,sepz"\n")
# fun5(10,1,7,3,8,6,7,10)

# def fun5(*A,**b):
#     print(a,b,sep"\n")
# fun5(10,1,7,3,8,6,b=30)
# it gives an error because we take as first positional and next keyword so  we have to call fun also like in the format of first positional and keyword

# even numbers sum


# def fun2(*a):
#     sum=0
#     for i in a:
#       if  i%2==0:
#           sum+=i
#     print(sum)
# fun2(1,2,3,4,5,6)
# def fun8(*a):
#     sum=0
#     c=0
#     for i in a:
#         if c % 2 == 1:
#              sum+=1
#           c=c+1
#      print(sum)
# fun8(1,2,3,4,5,6)

a=(1,2,3,4,5,7,7,8,8,10)
print(sum(a[1:6:2]))