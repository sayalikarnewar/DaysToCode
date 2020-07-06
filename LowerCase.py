#Write a Python program to check whether lowercase letters exist in a string.

string = "SWAROOP a."
string = list(string)
for i in string:
    if ord(i)>=97 and ord(i)<=122:
        print(True)
        break
    else:
        continue;
