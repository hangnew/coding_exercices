# 문자열을 입력하고 입력된 문자열의 문자를 앞뒤로 번갈아 출력하는 프로그램을 작성하십시오.

# 입력 : 임의의 문자열 (100자 이내)
# 출력 : 입력된 문자열의 앞과 뒤가 번갈아 출력된 형태

words = input()
for i in range(len(words)):
	j = len(words) - i - 1
	if i > j:
		break
	elif i == j:
		print(words[i], end='')
	else:
		print(words[i] + words[j], end='')
