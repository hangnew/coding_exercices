# 푸시(push)와 팝(pop)으로 스택에 자료를 넣고 빼는 작업을 진행하고 스택의 마지막 상태를 출력하는 프로그램을 작성하시오.
# 스택은 최대 10개의 자료가 들어갈 수 있고, 10개를 넘으면 overflow를 출력합니다.
# 스택이 비어있는 상태에서 pop을 실행하면 underflow를 출력합니다.
# 프로그래밍 언어에서 제공하는 라이브러리를 사용하지 않고 문제를 해결하는 것을 권장합니다.

# 첫 줄에 데이터 입력 횟수 입력
# 다음 줄부터 0인 경우 푸시, 1인 경우 팝 (overflow, underflow 고려)
# 0 또는 1 이외의 것을 입력하면 프로그램 종료
# 푸시인 경우에만 자료의 내용을 다음 줄에 입력

stack = []
loop = int(input())
for _ in range(loop):
	choice = int(input())
	if choice == 0:
		if len(stack) < 10:
			stack += [int(input())]
		else:
			print('overflow')
	elif choice == 1:
		if len(stack) != 0:
			# stack.pop()
			del stack[-1]
		else:
			print('underflow')
	else:
		break

for i in range(len(stack)):
	print(stack[i], end = ' ')
