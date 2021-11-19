# 현재 필드에 N개의 뿌요가 일렬로 늘어서 있는 상태이다.
# M개 이상의 뿌요가 서로 인접해 있으면 터지며, 가장 왼쪽에 있는 뿌요가 먼저 터진다는 조건이 있다.
# 더 이상 터질 수 있는 뿌요가 없게 된 최종 상태를 출력해보자.

# 첫째 줄에 정수 N과 M이 주어진다.
# 둘째 줄에 길이 N의 뿌요 문자열이 주어진다. 이 문자열은 영어 대문자로만 이루어져 있다.
# 뿌요가 터지고 난 후 최종 상태의 뿌요 문자열을 출력한다.
# 이때, 모든 뿌요가 터져서 남아있는 뿌요가 없는 경우 "CLEAR!" 출력한다.

import re

def clear(n, m, puyos):
		idx = 0
		while idx < len(puyos):
			combo = 0;
			first_char = puyos[idx]
			while first_char == puyos[idx + combo]:
				combo += 1
				if idx + combo > len(puyos) - 1:
					break
			if combo >= m:
				p = '[%c]{%d,}' % (first_char, m)
				pattern = re.compile(p)
				puyos = pattern.sub('', puyos, count = 1)
				idx = 0
				continue
			idx += 1
		puyos = 'CLEAR!' if len(puyos) == 0 else puyos
		print(puyos)

[n, m] = list(map(lambda x: int(x), input().split()))
puyos = input()
if n == m:
	print(puyos)
else:
	clear(n, m, puyos)
