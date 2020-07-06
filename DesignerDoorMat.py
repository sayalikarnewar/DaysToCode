n, m = map(int, input().split(" "))
d = '-'
c = '.|.'
for i in range(n//2): #before welcome
    print((c*(i)).rjust(m//2-1,d) + c + (c*(i)).ljust(m//2-1,d))

print("WELCOME".center(m,d))  #welcome

for i in range(n//2): #after welcome
    print((c*(n//2-i-1)).rjust(m//2-1,d) + c + (c*(n//2-i-1)).ljust(m//2-1,d))

'''
i/o
7 21
---------.|.---------
------.|..|..|.------
---.|..|..|..|..|.---
-------WELCOME-------
---.|..|..|..|..|.---
------.|..|..|.------
---------.|.---------
'''
