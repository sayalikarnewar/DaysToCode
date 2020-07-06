#Your task is to wrap the string s into a paragraph of width w

import textwrap

def wrap(string, max_width):
    test = textwrap.fill(string,width=max_width)
    text = textwrap.wrap(string,width=max_width)
    return test, text
if __name__ == '__main__':
    string, max_width = input(), int(input())
    result, results = wrap(string, max_width)
    print(result, results)
    
    
    
'''
io
shfiueyfqieuyf owfyerifu r fiquf wour
5
shfiu
eyfqi
euyf 
owfye
rifu
r
fiquf
wour ['shfiu', 'eyfqi', 'euyf ', 'owfye', 'rifu', 'r', 'fiquf', 'wour']
'''
