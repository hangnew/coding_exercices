# 한 변의 길이가 N인 정사각형 모양의 격자판이 있다.
# 이 격자판의 각 격자는 길이가 1일 때, 이 격자판의 크고 작은 정사각형의 개수는 총 몇 개일까?

def squares(n):
	result = 0
	for i in range(1, n + 1):
		result += i * i
	return result

n = int(input())
print(squares(n))
