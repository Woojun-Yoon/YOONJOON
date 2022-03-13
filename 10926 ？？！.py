a = input()
print(a + '??!')

# readline을 사용하면 안되는 이유
# readline은 개행 문자를 포함하여 입력을 한 줄 받아옴으로 
# woojun을 입력하면 입력된 데이터는 woojun\n이다
# 따라서, 데이터의 양끝 공백문자 및 개행문자를 지워주는 strip()을 사용하면됨
# EX) a = sys.stdin.readline().strip()


