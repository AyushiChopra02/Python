from sys import stdin


def swapAlternate(arr, n):
    #Your code goes here
    length = len(arr)
    if length == 1:
        print(arr)
    else:
        for i in range(0, length-1, 2):
            arr[i], arr[i+1] = arr[i+1], arr[i]



def takeInput():
    n = int(stdin.readline().rstrip())

    if n == 0 :
        return list(), 0

    arr = list(map(int, stdin.readline().rstrip().split(" ")))
    return arr, n



def printList(arr , n):
    for i in range(n):
        print(arr[i], end=" ")
    print()


#main
t = int(stdin.readline().rstrip())

while t > 0:
    arr, n = takeInput()
    if n != 0:
        swapAlternate(arr, n)
        printList(arr, n)
    t -= 1