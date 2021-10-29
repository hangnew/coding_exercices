# 이 문제는 반복문을 실습할 수 있는 피라미드 쌓기입니다. 입력한 수가 피라미드의 층수가 된다고 생각하고 '*'로 이루어진 피라미드 모양을 출력하는 프로그램을 작성하십시오.

n = int(input())
for i in range(0, n + 1):
	for _ in range(n - i - 1):
		print(' ', end='')
	for _ in range(2 * i + 1):
		print('*', end='')
	print()
