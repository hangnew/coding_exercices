# NxN 격자 모양의 공터에서 KxK 정사각형 크기의 땅을 구매하려고 할 때,
# 구매할 땅에 포함 된 폐기물의 수를 최소로 할 수 있는 영역을 찾을 수 있는 프로그램을 작성해보자

# 첫 줄에는 테스트케이스의 수를 나타내는 1 이상 100 이하의 자연수 T가 주어진다.
# 각 테스트케이스의 첫 줄에는 두 자연수 공터의 크기를 나타내는 N과 구매할 땅의 크기를 나타내는 K가 주어진다.
# 이후 N줄에 걸쳐서 공터의 각 행의 정보가 차례로 주어진다. 
# (0은 비어있는 땅을 나타내며, 1은 폐기물이 존재하는 칸을 나타낸다)

# 각 테스트케이스에 대하여 KxK 모양의 땅을 구매했을 때 얻을 수 있는 최소의 폐기물의 수를 공백없이 한 줄에 출력한다.

case_size = int(input())

def test_case(case_index):
	nk = list(map(lambda x: int(x), input().split())) # [n, k]
	wastes = [list(map(int, input().split())) for _ in range(nk[0])]
  
	loop = nk[0] - nk[1] + 1
	minimum = nk[1] ** 2
  
	for y in range(loop):
		for x in range(loop):
			temp_min = 0
			az = y + nk[1]
			for a in range(y, az):
				bz = x + nk[1]
				for b in range(x, bz):
					temp_min = temp_min + 1 if wastes[a][b] == 1 else temp_min
			minimum = temp_min if temp_min < minimum else minimum
	print(minimum)

for i in range(1, case_size + 1):
	test_case(i)
