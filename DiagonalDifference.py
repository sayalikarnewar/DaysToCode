#absolute difference between the sum of the diagonal elements of a square matrix

def diagonalDifference(arr):
    n = len(arr)
    d1, d2 = 0,0
    
    for i in range(n):
        for j in range(n):
            if i==j:
                d1+=arr[i][j]
            if i+j==n-1:
                d2+=arr[i][j]
            
    return abs(d1-d2)

if __name__ == '__main__':
    n = int(input().strip())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
    
    result = diagonalDifference(arr)
    print(result)


'''
i/o
3
11 2 4
4 5 6
10 8 -12
15
'''
