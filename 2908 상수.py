from sys import stdin
input = stdin.readline

list = input().rstrip()

a = int(list[2]) * 100 + int(list[1]) * 10 + int(list[0])
b = int(list[6]) * 100 + int(list[5]) * 10 + int(list[4])

if a > b:
    print(a)
else:
    print(b)

'''
num1=list(input())
num2=list(input())

num1.reverse()
num2.reverse()

a= int(num1[0]+num1[1]+num1[2])
b= int(num2[0]+num2[1]+num2[2])
print(max(a,b))
'''
