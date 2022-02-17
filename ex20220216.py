# 주사위를 순서대로 정렬시켜보니 각 변의 길이가 1부터 N까지 모두 있는 것을 알게되었다.
# 현재 모든 주사위의 부피의 합은 얼마일까?

n = int(input())
sumsum = n * (n + 1) // 2           # 가우스
print(sumsum ** 2 % 1000000007)