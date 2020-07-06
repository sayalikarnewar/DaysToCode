#Write a Python program to remove and print every third number from a list of numbers until the list becomes empty.

numbers = [386, 462, 8, 918, 237,17, 104,51, 742, 717,958,743, 527]
new = []
for i in range(len(numbers)-1):
    if i%3==2:
        new.append(numbers[i])
print("removed items are :",new)                
for i in numbers:
    if i in new:
        numbers.remove(i)
print("updated list is :",numbers)

'''
OUTPUT
removed items are : [8, 17, 742, 743]
updated list is : [386, 462, 918, 237, 104, 51, 717, 958, 527]
'''
