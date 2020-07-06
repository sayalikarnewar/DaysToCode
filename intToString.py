#Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn

n = 4
op = int("%s" %n) + int("%s%s" % (n,n)) + int("%s%s%s" %(n,n,n))
print(op)

#output
#492
