# 채팅방에 들어오고 나가거나, 닉네임을 변경한 기록이 담긴 문자열 배열 record가 매개변수로 주어질 때,
# 모든 기록이 처리된 후, 최종적으로 방을 개설한 사람이 보게 되는 메시지를 문자열 배열 형태로 return하도록 solution 함수를 완성하라

def solution(record):
    answer = []
    users = {}
    for item in record:
        cmd = item.split()[0]
        if (cmd != 'Leave'):
            id = item.split()[1]
            name = item.split()[2]
            users[id] = name
    for item in record:
        cmd = item.split()[0]
        post = '님이 들어왔습니다.' if cmd == 'Enter' else '님이 나갔습니다.'
        id = item.split()[1]
        if (cmd != 'Change'):
            result = users[id] + post
            answer.append(result)
    return answer
