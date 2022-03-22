from sys import stdin
input = stdin.readline

n = int(input())
book_dict = {}
result_list = []
count = 0
for _ in range(n):
    book = input().rstrip()
    if book in book_dict:
        book_dict[book] += 1
    else:
        book_dict[book] = 1

for item in book_dict.items():
    book_name, book_num = item
    if book_num > count:
        count = book_num
        result_list = []
        result_list.append(book_name)
    elif book_num == count:
        result_list.append(book_name)

print(sorted(result_list)[0])
