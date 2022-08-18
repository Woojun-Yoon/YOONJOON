from sys import stdin
input = stdin.readline
import re

if __name__ == '__main__':
    poly = input().rstrip()
    x = re.findall('-?\d+x', poly)
    c = re.findall('[-, +]?\d+$', poly)
    result = ''

    if poly == '0':
        result = 'W'
    else:
        if x:
            n = str(int(x[0][:-1]) // 2)
            if n[0] == '-':
                sign = '-'
            else:
                sign = ''
            
            if n in ['1', '-1']:
                result += sign + 'xx'
            else:
                result += n + 'xx'
        
        if c:
            n = c[0]
            if n not in ['+0', '-0']:
                if n[0] == '-':
                    sign = '-'
                else:
                    sign = '+'
                
                if n == '1':
                    result += 'x'
                elif n in ['-1', '+1']:
                    result += sign + 'x'
                else:
                    result += n + 'x'
        
        result += '+W'
    
    print(result)
