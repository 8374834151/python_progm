a=int(input())
b=int(input())
for i in range(a,b+1):
    if i %2==0:
        print(i,end=" ")

a=1
b=35
for i in range(a,b+1):
    if i %2==1:
        print(i,end=" ")

n=338
if n%2==0:
    print("even")
else:
    print("odd")

a=int(input())
b=int(input())
sum =0
for i in range(a,b+1):
    if i %2==1:
        sum=sum+i
print(sum)
a=int(input())
b=int(input())
sum=0
c=0
for i in range(a,b+1):
    if i%2==0:
        sum=sum+i
        c=c+1
print(sum/c)

# sum of alternative even numbers
a=int(input())
b=int(input())
sum=0
c=0
for i in range(a,b+1):
    if i %2==0:
         c=c+1
         if c%2==1:
            sum=sum+i
print(sum)
# alternative even numbers
a=int(input())
b=int(input())
c=0
for i in range(a,b+1):
    if i %2==0:
         c=c+1
         if c%2==1:
            print(i)


a=int(input())
b=int(input())
c=0
sum=0
count=0
for i in range(a,b+1):
    if i%2==0:
        c=c+1
        if c%2==1:
            sum=sum+i
            count=count+1
            avg=sum/count
print(avg)