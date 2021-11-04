# 입력된 수가 소수(Prime Number)인지를 판별하는 프로그램을 작성하십시오.
# O(\sqrt{n})의 시간에 동작하는 알고리즘으로 문제를 해결하는 것을 권장합니다.

import math

def isPrime(n):
	if n == 1:
		return False
	if n % 2 == 0:
		return True if n == 2 else False
	for i in range(3, int(math.sqrt(n)), 2):
		if n % i == 0:
			return False
	return True

n = int(input())
print(isPrime(n))
