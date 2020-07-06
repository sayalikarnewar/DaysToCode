#Reverse words in a given string

string = list(map(str, input().split(".")))
string.reverse()
print(".".join(string))

'''
i/o
helo.saya.k
k.saya.helo
'''
