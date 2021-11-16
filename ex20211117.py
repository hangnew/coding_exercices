# 정렬된 배열 A, B가 주어지면 배열을 합친 후 다시 정렬하는 프로그램을 작성하십시오.
# 1. 첫 번째 줄에 배열 A, B의 크기 순서대로 입력
# 2. 다음 줄에 배열 A의 내용, 그 다음 줄에 배열 B의 내용 입력
# 3. 두 배열을 합친 결과를 출력한다.

input()
arr = list(map(lambda x: int(x), input().split()))
arr += list(map(lambda x: int(x), input().split()))
for i in range(1, len(arr)):
	for j in range(len(arr) - 1):
		if arr[j] > arr[j + 1]:
			arr[j], arr[j + 1] = arr[j + 1], arr[j]
for n in arr:
	print(n, end=' ')
