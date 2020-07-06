#Write a Python program to accept a filename from the user and print the extension of that

data = "hello.java"
li = list(data)
ext = [li[(li.index("."))+1:] for i in li if i=='.']
l = ext[0]
print(*l, sep="")

#OUTPUT
#java
