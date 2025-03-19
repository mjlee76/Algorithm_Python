from collections import deque

def solution(priorities, location):
    queue = deque([idx, p] for idx, p in enumerate(priorities))
    
    count = 0
    while queue:
        current = queue.popleft()
        
        if any(current[1] < q[1] for q in queue):
            queue.append(current)
        else:
            count += 1
            if location == current[0]:
                return count

# 우선순위가 담긴 priorities와 몇번째로 실행되는지 알고싶은 갑인 location이 주어짐
# 큐에 프로세스들이 들어가고 하나의 프로세스를 제거할때 우선순위가 그보다 높은것이 있다면 다시 큐에 넣음
# location에 저장된 인덱스의 priorities 값이 몇번째로 실행되는지 return

# queue를 사용(선입선출)

# queue에 priorities의 인덱스와 값을 동시에 꺼내 튜플형태로 저장 (idx, p)

# popleft()했을 때 queue에 들어있는값중 우선순위가 높은게 있으면 다시 queue에 append,

# 우선순위가 높은게 없으면 count(실행순서)를 1늘려주고 location과 current[0](idx)와 비교해 같으면 count를 return
