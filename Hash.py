'''
7. Given an integer, , and  space-separated integers as input, create a tuple, , of those  integers. Then compute and print the result of hash()
Input Format
..  The first line contains an integer, , denoting the number of elements in the tuple.
    The second line contains  space-separated integers describing the elements in tuple .

Output Format - Print the result of hash()
Sample Input:
        2
        1 2
Sample Output:
        3713081631934410656
'''

if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    integer_list = tuple(integer_list)
    print(hash(integer_list))
    
    
'''
output
2
1 2
3713081631934410656
'''
