# Read input as sepcified in the question
# Print output as specified in the question
n=int(input())
li=[int(x) for x in input().split()]
sum=0
for i in range(n) :
    sum=sum+li[i]
print(sum)