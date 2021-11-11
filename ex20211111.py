# 집 주변에 위치한 N개의 매점에서 N-2개의 물건을 사야한다.
# 집에서 출발하여 (N-2)개의 매점에서 필요한 물건을 1개씩 구매하고자 할 때, 최소한 적은 거리를 이동해야 한다.

# 1. 첫째 줄에 매점의 개수를 나타내는 정수 N과 집의 위치를 나타내는 정수 x가 공백으로 구분되어 주어진다.
# 2. 둘째 줄에 매점의 위치 p1, p2, ... pN가 공백으로 구분되어 주어진다
# 3. N-2개의 물품을 사기 위해 이동해야 하는 거리의 최소값을 출력한다.


def shortcut(n, x, p):
	items = n - 2 if n - 2 > 0 else 0	# 사야할 물건 개수 (한 블럭당 매점 개수)
	loop = 3 if n > 2 else 0	# 반복할 회수
	
	# 첫 번째 블럭 (길이 : items) 최단 거리 (사야할 물건이 0일 경우 0)
	result = 0
	if items > 0: # 사야할 물건이 1개 이상인 경우
		distance1 = abs(p[items - 1] - p[0]) # 블럭의 마지막 매점에서 첫 번째 매점까지 거리
		from_first1 = abs(p[0] - x) # 집에서 첫 번째 매점까지의 거리
		from_last1 = abs(p[items - 1] - x) # 집에서 마지막 매점까지의 거리
		start_point1 = from_first1 if from_first1 < from_last1 else from_last1 # 더 짧은 거리의 매점부터 출발
		result = distance1 + start_point1	# 총 거리 = 매점끼리의 총 거리 + 집에서 시작 매점까지의 거리
	
	# 두 번째 블럭부터 총 거리가 result보다 짧은지 비교
	for i in range(1, loop):
		distance = abs(p[i + items - 1] - p[i])
		from_first = abs(p[i] - x)
		from_last = abs(p[i + items - 1] - x)
		start_point = from_first if from_first < from_last else from_last
		temp_result = distance + start_point
		result = temp_result if temp_result < result else result
	
	print(result)
	
  
[num_shops, my_location] = list(map(lambda x: int(x), input().split())) # [매점개수, 집 위치]
shops_loc = list(map(lambda x: int(x), input().split())) # 매점의 위치
shops_loc.sort() # 오름차순 정렬
shortcut(num_shops, my_location, shops_loc)
