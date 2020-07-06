#Write a Python function to find a distinct pair of numbers whose product is odd from a sequence of integer values

numbers = [2,3,4,5,6]
pairs = []
for i in numbers:
    for j in numbers:
        if i*j%2==1:
            lis = [i,j]
            pairs.append(lis)
print(pairs)            

#[[3, 3], [3, 5], [5, 3], [5, 5]]
