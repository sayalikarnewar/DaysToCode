#22. Pattern staircase right shifted pyramid

def staircase(n):
    for i in range(1,n+1):
        print(" "*(n-i)+"#"*i)
    
    
if __name__ == '__main__':
    n = int(input())

    staircase(n)

'''
i/o
4
   #
  ##
 ###
####
'''
