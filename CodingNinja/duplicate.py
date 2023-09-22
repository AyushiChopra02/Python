def duplicate (list1,sum):
    sum_time=0
    size=len(list1)
    for i in range(0,size):
        for j in range(i+1,size):
            if list1[i] + list1[j]==sum:
                sum_time+=1
            else:
                continue
    print(sum_time)

n=int(input()) 
for i in range(n):
    faltu1=int(input()) #Secound input #no of ele in list
    if faltu1!=0:
        list = [int(x) for x in input().split()]
    X=int(input()) #3rd Input
    if faltu1!=0 :
        duplicate(list,X)
    else:
        print(0)