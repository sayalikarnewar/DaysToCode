#Write a Python program to add two objects if both objects are an integer type. 

a,b = input(), input()
try:
    a = int(a)
    b = int(b)
    print("sum :",a+b)
except:
    print("ValueError")
