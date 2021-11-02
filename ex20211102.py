# 혜지는 자신의 컴퓨터로 코딩을 하던 중, 자신의 코드가 통째로 지워지는 현상을 겪었다. 
# 여러 번의 시행착오 끝에, 키보드를 마지막으로 누른 후 c초 동안 자신의 코드가 그대로 남아있다가 (c+1)초가 경과하는 순간 모든 코드가 지워지는 것을 알게 되었다. 
# 혜지는 오기가 생겨 과연 자신의 코드가 지워지는게 먼저인지 아니면 자신이 코드를 완성하는 게 먼저인지 자신의 고장난 컴퓨터와 대결해보고 싶었다. 
# 혜지가 키보드를 총 N번 누른다고 할 때, 코딩을 시작한 이후 몇 초가 경과하고 키보드를 쳤는지에 대한 N개의 정보를 이용하여 코딩을 마쳣을 때 총 몇 글자가 남아있는지 계산하여라.

n = list(map(lambda x: int(x), input().split())) # n, c
t = list(map(lambda x: int(x), input().split())) # t[0], t[1], t[2] ...

def countdown(second, array):
	count = 1
	for i in range(0, len(array) - 1):
		if array[i + 1] - array[i] <= second:
			count += 1
		else:
			count = 1
	print(count)
	
countdown(n[1], t)
