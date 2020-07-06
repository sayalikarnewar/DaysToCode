def gcd(a,b):
    while(b):
        a,b = b,a%b
    return a
    
def lcm(a,b):
    lcm = (a*b)//gcd(a,b)
    return lcm
    
lcm(30,6)

#30
