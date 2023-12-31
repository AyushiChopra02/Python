# @Kunalbhatia-Hub

from sys import stdin

def pushZerosAtEnd(arr, n) :
    next=0

    for i in range(n):
        if arr[i] != 0 :
            arr[i], arr[next] = arr[next], arr[i]
            next+=1


#Taking Input Using Fast I/O
def takeInput() :
    n = int(stdin.readline().rstrip())

    if n == 0:
        return list(), 0
    
    arr = list(map(int, stdin.readline().rstrip().split()))
    return arr, n
  


def printList(arr, n) : 
    for i in range(n) :
        print(arr[i], end = " ")

    print()



t = int(stdin.readline().strip())

while t > 0 :

    arr, n = takeInput()

    pushZerosAtEnd(arr, n)
    printList(arr, n)

    t -= 1

