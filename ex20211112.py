# 배열에 들어있는 정수 중 최소값을 구하는 프로그램을 작성하십시오.

input()
arr = list(map(lambda x: int(x), input().split()))
print(min(arr))
