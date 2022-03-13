from sys import stdin
input = stdin.readline
'''
word_count = 0
word = input().strip()
for i in range(len(word)):
    if (word[i] == 'c' or word[i] == 's' or word[i] == 'z') and (len(word) - i > 1):
        if word[i + 1] == '=' or word[i + 1] == '-':
            word_count = word_count
        else:
            word_count += 1
    elif (word[i] == 'd') and (len(word) - i > 1):
        if word[i + 1] == '-':
            word_count = word_count
        elif word[i + 1] == 'z' and (len(word) - i > 2):
            if word[i + 2] == '=':
                word_count = word_count
            else:
                word_count += 1
        else:
            word_count += 1
    elif word[i] == 'l' and (len(word) - i > 1):
        if word[i + 1] == 'j':
            word_count = word_count
        else:
            word_count += 1
    elif word[i] == 'n' and (len(word) - i > 1):
        if word[i + 1] == 'j':
            word_count = word_count
        else:
            word_count += 1
    else:
        word_count += 1
print(word_count)
'''
a = input().strip(); print(len(a) - sum(map(a.count,['-','=','lj','nj','dz='])))
