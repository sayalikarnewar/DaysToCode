#successfully blow out the tallest candles
def birthdayCakeCandles(ar):
    ar = sorted(ar)
    print(ar.count(ar[-1]))
if __name__ == '__main__':
    
    ar_count = int(input())
    ar = list(map(int, input().rstrip().split()))
    result = birthdayCakeCandles(ar)
    
'''
i/o
4
2 1 4 4
2
'''
