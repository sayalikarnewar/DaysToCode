#17. Write a Python program to test whether a number is within 100 of 1000 or 2000.

num = 2101
if abs(num-1000)<=100 or abs(num-2000)<=100:
    print(True)
else:
    print(False)
    
#output - false    
