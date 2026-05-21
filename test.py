# num=input("enter the number:")
# print(type(num))
# if int(num)%2==0:
#     print(num,"true")
# else:
# #     print(num,"false")
#
# amount = int(input("Enter the number: "))
# if amount <= 1000:
#     tip = amount + int( 20//100 )
#     print( tip)
#     exit()
# if amount >1001 & amount <= 2000:
#     tip = amount + int( 30//100 )
#     print(tip)
#     exit()
# if amount >2001 & amount <= 5000:
#     tip = amount //40
#     print(tip)

bill=float(input("what was the total bill? "))
tip=int(input("what percentage tip would you like to give?10 12 15"))
if bill<=1000:
    tip=tip/100

