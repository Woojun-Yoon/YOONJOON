if __name__ == '__main__':
    while (1):
        try:
            a, b = map(int, input().split())
            print(b // (a + 1))
        except EOFError:
            break