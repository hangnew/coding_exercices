임의의 대회에 출전한 한 사람의 등수 내역을 순서대로 나열한다. (1 이상 9 이하)
등수를 나열한 이 문자열에서 "12"와 "21"의 부분 문자열이 각각 1번 이상 존재하면 참, 그렇지 않다면 거짓이다.
이 문자열이 서로 겹쳐서는 안 된다.

1. 첫째 줄에 1 이상 9 이하의 숫자로 이루어진 문자열이 주어지며, 이 문자열의 길이는 1 이상 10^5 이하이다.
2. 연구결과가 참이면 Yes, 거짓이면 No를 출력한다.

grades = input()

if grades.find('21') < grades.find('12'):
	result = 'Yes' if grades.replace('21', '', 1).find('12') > -1 else 'No'
else:
	result = 'Yes' if grades.replace('12', '', 1).find('21') > -1 else 'No'
  
print(result)
