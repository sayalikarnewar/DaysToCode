'''
6. Consider a list (list = []). You can perform the following commands:
    insert i e: Insert integer  at position .
    print: Print the list.
    remove e: Delete the first occurrence of integer .
    append e: Insert integer  at the end of the list.
    sort: Sort the list.
    pop: Pop the last element from the list.
    reverse: Reverse the list.
----------------------------------------------------------
    The first line contains an integer, , denoting the number of commands.Each line  of the  subsequent lines contains one of the commands described above.
    The elements added to the list must be integers.
    For each command of type print, print the list on a new line.     
Sample Input:
    12
    insert 0 5
    insert 1 10
    insert 0 6
    print
    remove 6
    append 9
    append 1
    sort
    print
    pop
    reverse
    print
Sample Output 0
    [6, 5, 10]
    [1, 5, 9, 10]
    [9, 5, 1]
'''

if __name__ == '__main__':
    N = int(input())
    lis = []
    prin = []
    for i in range(N):
        command = input().split()
        lis.append(command)
    
    for i in lis:
        if i[0]=="insert":
            prin.insert(int(i[1]),int(i[2]))
        elif i[0]=='print':
            print(prin)
        elif i[0]=='remove':
            prin.remove(int(i[1]))    
        elif i[0]=='pop':
            prin.pop(-1)
        elif i[0]=='append':
            prin.append(int(i[1]))
        elif i[0]=='sort':
            prin.sort()
        elif i[0]=='reverse':
            prin.reverse()
        else:
            continue    
