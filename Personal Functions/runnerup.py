'''
oct 2018
author: Casey

prints 2nd largest integer given to it in an array, removing all duplicates of the largest integer
'''

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    
    arr.sort()
    curMax=arr[-1]
    while curMax in arr:
        arr.remove(arr[-1])
    print(arr[-1])

