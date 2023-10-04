def triplesum (list1,sum):
    sum_time=0
    n=len(list1)
    for i in range(0,n):
        for j in range(i+1 ,n):
            for k in range(j+1,n):
                if list1[i] + list1[j]+ list1[k]==sum:
                    sum_time+=1
                else:
                    continue
    print(sum_time)

n=int(input())
for i in range(n):
    faltu1=int(input())
    if faltu1!=0:
        list = [int(x) for x in input().split()]
    X=int(input())
    if faltu1!=0 :
        triplesum(list, X)
    else :
        print(0)