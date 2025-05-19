import heapq
def solution(operations):
    answer = []
    heapq.heapify(answer)
    
    for oper in operations:
        command, value = oper.split()
        value = int(value)
        
        if command == 'I':
            heapq.heappush(answer, value)
        elif command == 'D' and len(answer) != 0:
            if value == -1:
                heapq.heappop(answer)
            else:
                max_val = max(answer)
                answer.remove(max_val)
                heapq.heapify(answer)
    
    if len(answer) == 0:
        return [0, 0]
    
    else: 
        return[max(answer), min(answer)]


# 우선순위큐(heapq)사용
# 파이썬의 heapq는 최소힙(Min heap)
# 최소힙은 작은값이 가장 우선순위가 높음(가장 앞에 옴)

# 최소값 삭제시 그냥 heapq.heappop() 이용
# 최대값 삭제시 max()함수로 최대값 찾아서 삭제 후, 다시 heapify로 최소힙으로 재변환
# 최대값 삭제시 최대힙(Max heap: 모든값을 음수로 바꾸면 됨)으로 구현 가능하나 여기선 max함수로 간단하게 구현
