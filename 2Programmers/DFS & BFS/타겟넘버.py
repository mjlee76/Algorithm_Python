def solution(numbers, target):
    answer = 0
    q = [[numbers[0],0], [-1*numbers[0],0]]
    n = len(numbers)
    while q:
        temp, idx = q.pop()
        idx += 1
        if idx < n:
            q.append([temp + numbers[idx], idx])
            q.append([temp - numbers[idx], idx])
        else:
            if temp == target:
                answer += 1
    return answer


# BFS 사용
# 큐에 첫값 1과 -1을 넣고(idx도 함께 넣음) 스택처럼 pop()
# 