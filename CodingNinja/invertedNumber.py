n=int(input())
r=1
while r<=n :
    c=1
    while c<=(n-r+1):
        print(n-r+1,end="")
        c+=1
    print()
    r+= 1