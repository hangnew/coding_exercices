# 길이가 N인 수열이 있다.
# M개의 숫자가 주어졌을 때 그 숫자가 수열에 등장했으면 1, 등장하지 않으면 0을 출력한다.

int(input())
ns = set(map(lambda x: int(x), input().split()))
int(input())
ms = list(map(lambda x: int(x), input().split()))

def match(set1, list1):
	for m in list1:
		if m in set1:
			print(1)
		else:
			print(0)

match(ns, ms)
