#Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.

def timeConversion(s):
    if s[-2:] == 'AM' and s[:2]=='12':
        return '00'+s[2:-2]
    elif s[-2:] == 'AM':
        return s[:-2]
    elif s[-2:] =='PM' and s[:2]=='12':
        return s[:-2]
    elif s[-2:] == 'PM':
        hours = int(s[:2]) + 12
        return str(hours)+s[2:-2]

if __name__ == '__main__':
    s = input()

    result = timeConversion(s)
    print(result)
    

'''
i/o
00:00:00PM
12:00:00
'''
