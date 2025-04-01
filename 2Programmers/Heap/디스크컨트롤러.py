import heapq
def solution(jobs):

    jobs.sort()
    
    time = 0
    total_time = 0 # 평균구하기 위한 전체 시간합
    count = 0      # 평균구하기 위한 전체 작업 개수
    waiting_jobs = []
    i = 0
    n = len(jobs)
    
    while i < n or len(waiting_jobs) != 0:
        while i < n and jobs[i][0] <= time:
            heapq.heappush(waiting_jobs, (jobs[i][1], jobs[i][0]))
            i += 1

        if len(waiting_jobs) != 0:
            processT, requestT = heapq.heappop(waiting_jobs)
            time += processT
            total_time += (time - requestT)
            count += 1
        else:
            time = jobs[i][0]
            
    return total_time // count

# **우선순위 큐(Heap)**를 사용하여 작업 처리 시간이 짧은 작업부터 처리합니다.

# 현재 시간에 도달한 작업들은 모두 큐에 넣고, 처리 가능한 작업을 큐에서 꺼내서 처리합니다.

# 대기 중인 작업이 없으면 새로운 작업 요청 시간까지 기다립니다.

# 모든 작업이 처리된 후, 소요 시간을 계산하고 평균을 구하는 방식으로 최종 결과를 도출합니다.