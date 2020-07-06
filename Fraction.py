#Fraction of positive, negative and zero in an array

def plusMinus(arr):
    pos = []
    neg = []
    zero = []
    n = len(arr)
    for i in arr:
        if i<0:
            neg.append(i)
        elif i>0:
            pos.append(i)
        elif i==0:  
            zero.append(i)
    print("{:.6f}".format(len(pos)/n))
    print("{:.6f}".format(len(neg)/n))
    print("{:.6f}".format(len(zero)/n))
    
if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().split()))

    plusMinus(arr)

'''
i/o
5
1 1 0 -1 -1
0.400000
0.400000
0.200000
'''
