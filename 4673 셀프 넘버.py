# 브루트포스 알고리즘

def self_number(n):
	if 0<n<10:
		return n + n
	elif 10 <= n <= 99:
		str_n = str(n)
		return n + int(str_n[0])+ int(str_n[1])
	elif 100 <= n <= 999:
		str_n = str(n)
		return n + int(str_n[0])+ int(str_n[1]) + int(str_n[2])
	elif 1000 <= n <= 9999:
		str_n = str(n)
		return n + int(str_n[0])+ int(str_n[1]) + int(str_n[2]) + int(str_n[3])
	else:
		str_n = str(n)
		return n + int(str_n[0])+ int(str_n[1]) + int(str_n[2]) + int(str_n[3]) + int(str_n[4])

num_list = [0] * 10000

for i in range(1, 10000, 1):
	return_num = self_number(i)
	if return_num <= 9999:
		num_list[return_num] += 1
	
for j in range(1, 10000, 1):
	if num_list[j] == 0:
		print(num_list.index(0, j)) #index(value, start, end)