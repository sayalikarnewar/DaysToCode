'''
Given an integer, , print the following values for each integer  from  to :
    Decimal
    Octal
    Hexadecimal (capitalized)
    Binary
    '''
    
def print_formatted(number):
    for i in range(1,n+1):
        dec = str(i)
        octal = str(oct(i))[2:]
        hexa = str(hex(i))[2:].upper()
        binary = str(bin(i))[2:]
        k = len(str(bin(n))[2:]) 
        print(dec.rjust(k," ")+" "+octal.rjust(k," ")+" "+hexa.rjust(k," ")+" "+ binary.rjust(k," "))
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)    
    
'''
i/o
11
   1    1    1    1
   2    2    2   10
   3    3    3   11
   4    4    4  100
   5    5    5  101
   6    6    6  110
   7    7    7  111
   8   10    8 1000
   9   11    9 1001
  10   12    A 1010
  11   13    B 1011
  '''
