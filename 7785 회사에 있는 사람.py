from sys import stdin
input = stdin.readline

company = set([])
for _ in range(int(input())):
    name, com = input().split()
    if com == "enter":
        company.add(name)
    elif com == "leave":
        company.remove(name)
company = sorted(list(company), reverse = 1)
print('\n'.join(company))