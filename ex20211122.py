# 첫 줄에 램프의 세로 길이 n과 가로 길이 m이 입력된다.
# 다음에는 n*m의 램프가 입력되며, 켜진 램프는 1, 꺼진 램프는 0으로 입력된다.
# 다음 줄에는 프로그래밍 하는 수(p)가 입력된다.
# 그 다음으로는 p개의 줄로, 가로는 0, 세로는 1과, 프로그래밍을 하는 줄이 입력된다.
# 단, 프로그래밍 하는 줄이 가로인 경우 n보다 작고, 세로인 경우 m보다 작다.

# 5, 8 runtime error

n, m = map(lambda x : int(x), input().split())
bulbs = [[False] * m] * n
for i in range(len(bulbs)):
	bulbs[i] = list(map(lambda x: bool(int(x)), input().split()))
	
p = int(input())
for _ in range(p):
	rc, ln = map(lambda x: int(x), input().split())
	ln -= 1
	if rc == 0:
		for j in range(len(bulbs[ln])):
			bulbs[ln][j] = not(bulbs[ln][j])
	else:
		for j in range(len(bulbs)):
			bulbs[j][ln] = not(bulbs[j][ln])

for bulb in bulbs:
	for result in bulb:
		result = 1 if result else 0
		print(result, end=' ')
	print()
