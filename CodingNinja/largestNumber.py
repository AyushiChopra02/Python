a= int(input())
b= int(input())
c= int(input())
if a>b and a>c:
    print("a is largest")
elif b>a and b>c:
    print("b is largest")
else:
    print(" c is largest")



    # nested if else
n= int(input())
m = int(input())
if n%2==0 :
    if m%2==0 :
        print(1)
    else:
        print(3) 
else :
    print(9)           



#while
n = int(input())
count = 1
while count <= n :
    print(count)
    count = count + 1 