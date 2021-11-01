# 지민이는 램을 모으는 것이 취미입니다. 램의 용량은 모두 2의 제곱수를 따르는데, 
# 어느 날 지민이가 사용하기 위해 꽂았던 임의의 램이 2의 제곱수를 따르지 않는 것을 알게 되었습니다. 
# 무슨 일인가 확인해보니 램이 일부분 파손되어 메모리가 제대로 표현이 되지 않는 것이었습니다. 
# 지민이는 속상했지만 파손된 램을 모두 찾아서 버리기로 결심했습니다.
# 하지만 지민이는 100 미만의 2의 제곱수는 알고 있지만, 100 이상의 수가 2의 제곱수인지 아닌지 판별할 수 없습니다. 
# 지민이가 100 이상의 용량을 가진 램 중 파손된 램의 개수와 번호를 찾을 수 있도록 도와주세요! 

num = int(input())
rams = input().split() # str

def damaged(n):
	n = int(n)
	while n % 2 == 0:
		n = n // 2
	if n != 1:
		return True
	return False

count = 0
damaged_list = ''
for i in range(0, len(rams)):
	if damaged(int(rams[i])):
		count += 1
		damaged_list += str(i + 1) + ' '
	
print(count)
print(damaged_list)
