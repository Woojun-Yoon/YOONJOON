if __name__ == '__main__':
    while True:    
        mem = [0 for _ in range(32)]
        result = 0
        pc = 0
        for _ in range(32):
            try:
                mem[_] = int(input(), 2)
            except EOFError:
                exit()
        
        while True:
            address = mem[pc]
            pc = (pc + 1) % 32
            com = address // 32
            value = address % 32

            if com == 0:
                mem[value] = result
            elif com == 1:
                result = mem[value]
            elif com == 2:
                if result == 0:
                    pc = value
            elif com == 4:
                result = (result - 1) % 256
            elif com == 5:
                result = (result + 1) % 256
            elif com == 6:
                pc = value
            elif com == 7:
                break
        
        print(format(result, 'b').zfill(8))