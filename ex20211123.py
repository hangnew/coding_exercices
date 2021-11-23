# N이 커짐에 따라 N!의 값이 얼마나 빨리 커지는지 잘 모르는 사람들에게 알려주기 위해
# N이 주어지면 N!의 맨 뒤에 붙는 연속한 0의 개수를 출력하는 프로그램을 작성 하려고 한다.
# 1. 첫째 줄에 정수 N이 주어진다.
# 2. N!의 맨 뒤에 붙는 연속한 0의 개수를 출력한다.

def zeros(number):
	count = 0
	while number >= 5:
		count += number // 5
		number //= 5
	print(count)

n = int(input())
zeros(n)
