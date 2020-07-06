#Write a Python program to create all possible strings by using 'a', 'e', 'i', 'o', 'u'. Use the characters exactly once.

from itertools import permutations
perm = permutations(vov,5)
for i in list(perm):
    print("".join(list(i)))
    
    
