1. 첫 줄에 배열의 숫자 개수
2. 다음 줄에 공백으로 구별하면서 배열에 수 입력
3. 합을 구하고자 하는 구간
4. 출력 : 구간의 합

input()
nums = list(map(lambda x : int(x), input().split()))
first, last = map(lambda x : int(x), input().split())
print(sum(nums[first - 1:last]))
