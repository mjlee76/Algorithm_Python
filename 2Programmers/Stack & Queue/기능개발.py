from collections import deque
import math

def solution(progresses, speeds):
    
    q = deque()
    
    for i in range(len(progresses)):
        days = math.ceil((100 - progresses[i]) / speeds[i]) # 남은 일수 계산
        q.append(days)
    
    answer = []
    first = q.popleft()
    count = 1
    while q:  # while len(q) != 0: 와 동일!
        if first < q[0]:
            answer.append(count)
            first = q.popleft()
            count = 1
        else:
            q.popleft()
            count += 1
    
    answer.append(count)
    
    return answer

# progresses에는 작업별 진행량이 적힌 배열, speeds에는 작업별 작업속도가 적혀있다. 작업은 우선순위로 적혀있고 
# 우선순위가 높은 작업이 100이되어 배포될때 뒤에 먼저 100이된 작업들이 함께 배포된다.
# 배포될때마다 몇개의 작업이 배포되는지 적힌 배열을 구하기

# ex) progresses=[93, 30, 55], speeds=[1, 30, 5] => return=[2, 1]

# 우선순위가 있으므로 큐를 사용한다.(FIFO: 선입선출)

# 먼저 배포까지 남은 일수를 계산하여 큐에 넣는다. ceil을 이용해 올림하여 남은 일수 계산 

# 큐에서 first = popleft()했을때 다음으로 나올 값(q[0])가 first보다 작으면 count늘려주고 또 빼준다.

# first보다 큰값이 q[0]가 되면 first를 해당값으로 초기화 & count = 1로 초기화 해준다.