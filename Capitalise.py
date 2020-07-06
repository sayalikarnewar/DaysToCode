#Capitalize the first letter of first and last name

def solve(s):
    s = s.split(" ")
    for i in range(len(s)):
        s[i] = s[i].capitalize()
    print(" ".join(s))    
if __name__ == '__main__':
    s = input()

    result = solve(s)    
#input
say k
#output
Say K
