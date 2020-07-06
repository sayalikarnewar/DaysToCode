#add all 0s from the list at the end of the list

def solve(A):
    for i in A:
        if i==0:
            A.remove(i)
            A.append(0)
                
    print A  

A = [1,2,0,4,0]
solve(A)

#output - [1,2,4,0,0]
