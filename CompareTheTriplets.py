#compare the triplets and count the points
a = list(map(int, input().rstrip().split()))
b = list(map(int, input().rstrip().split()))

def compareTriplets(a, b):
    countA = 0
    countB = 0
    for i in range(len(a)):
        if a[i]<b[i]:
            countB+=1
        elif a[i]>b[i]:
            countA+=1
        else:
            pass
    print(countA, countB)       

compareTriplets(a, b)    
'''
i/o

12 2 3
10 1 5
2 1
'''
