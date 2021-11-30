# 두 장소에 있던 N마리 쥐의 몸집 크기의 대푯값을 추출한다.
# (정수 X에 대해 쥐의 몸집 크기가 [x-2, x+2] 구간에 속하는 쥐가 가장 많을 때, 그 중 가장 작은 X값이 대푯값이 된다.
# 정우는 A장소의 대푯값이 B장소의 대푯값보다 더 클 것이라 기대하고 있다.

# 첫째 줄에 정수 N이 주어진다.
# 둘째 줄에 A장소에 있던 N마리의 쥐의 몸집 크기가 정수로 주어진다.
# 셋째 줄에 B장소에 있던 N마리의 쥐의 몸집 크기가 정수로 주어진다.

# 첫째 줄에 A장소의 대푯값, B장소의 대푯값을 공백으로 구분하여 출력한다.
# 둘째 줄에 정우의 예상이 들어맞았으면 'good', 그렇지 않다면 'bad'를 출력한다.

input()
samples_a = list(map(lambda x: int(x), input().split()))
samples_b = [int(x) for x in input().split()] # 기태법

def whosdaMax(lst):
	test_nums = [0] * (max(lst) - min(lst) + 5)
	loc = min(lst) - 2
	for sample in lst:
		idx = sample - loc
		test_nums[idx - 2] += 1
		test_nums[idx - 1] += 1
		test_nums[idx] += 1
		test_nums[idx + 1] += 1
		test_nums[idx + 2] += 1
	return test_nums.index(max(test_nums)) + loc

max_a = whosdaMax(samples_a)
max_b = whosdaMax(samples_b)

print(f'{max_a} {max_b}')
if max_a > max_b:
	print('good')
else:
	print('bad')
