#Write a Python program to count the number occurrence of a specific character in a string. 

char = input()
string = "my name is anthony gonsalvis."
string = list(string)
count = 0
for i in string:
    if i == char:
        count+=1
        
print(count)        

