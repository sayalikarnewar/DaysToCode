#Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers.

data = input()
la = data.split(",")
tu = tuple(la)
print(la, tu)

#outout
#1 2 3 4
#['1 2 3 4'] ('1 2 3 4',)
