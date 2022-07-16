from sys import stdin
input = stdin.readline

if __name__ == '__main__':
    count = 1

    while True:
        a, b, c = map(int, input().split())
        if a == 0 and b == 0 and c == 0:
            break
        
        if a == -1:
            cache = c ** 2 - b ** 2

            if cache <= 0:
                print("Triangle #", count, sep = '')
                print("Impossible.")
            else:
                print("Triangle #", count, sep = '')
                print("a ={: .3f}".format(cache ** 0.5))
            print()
            
        elif b == -1:
            cache = c ** 2 - a ** 2

            if cache <= 0:
                print("Triangle #", count, sep = '')
                print("Impossible.")
            else:
                print("Triangle #", count, sep = '')
                print("b ={: .3f}".format(cache ** 0.5))
            print()
        else: # c == -1
            cache = a ** 2 + b ** 2

            if cache <= 0:
                print("Triangle #", count, sep = '')
                print("Impossible.")
            else:
                print("Triangle #", count, sep = '')
                print("c ={: .3f}".format(cache ** 0.5))
            print()
    
        count += 1