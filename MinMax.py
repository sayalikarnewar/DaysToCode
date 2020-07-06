#Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers.

def miniMaxSum(arr):
    arr = sorted(arr)
    minSum = sum(arr[:-1])
    maxSum = sum(arr[1:])
    print(minSum, maxSum)
    
if __name__ == '__main__':
    arr = list(map(int, input().split()))

    miniMaxSum(arr)

'''
i/o
1 2 3 4 5
10 14
'''
