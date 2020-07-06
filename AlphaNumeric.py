#Check if atleast one alpha numeric, aplhabet, digit, lowercase , uppercase

s = input()
print(any(i.isalnum() for i in s))
print(any(i.isalpha() for i in s))
print(any(i.isdigit() for i in s))
print(any(i.islower() for i in s))
print(any(i.isupper() for i in s)) 

'''i/o
1aa
True
True
True
True
False'''
