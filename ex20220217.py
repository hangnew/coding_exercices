

# 공백으로 구분된 두 정수 N,K가 차례로 주어진다.
# N = 수열의 길이, K = 연속적인 정수의 개수
# 주어진 수열을 모두 같은 수로 만들고자 할 때 골라야 하는 최소 횟수를 출력한다.

import math
n, k = map(lambda x : int(x), input().split())
print(math.ceil((n - 1) / (k - 1)))

