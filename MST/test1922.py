# 1.아이디어
# - 컴퓨터 연결하는데 최소비용 : MST문제
# - 간선을 인접리스트에 넣기
# - 힙에 시작점 넣기
# - 힙이 빌때까지 다음 작업 반복:
#     - 힙의 최소값 꺼내서, 해당노드 방문하지 않았으면
#         - 방문표시, 비용값 추가, 연결된 간선들 힙에 넣기

import sys
import heapq
input = sys.stdin.readline

# 컴퓨터수 입력
V = int(input())

# 컴퓨터를 연결하는 간선수 입력
E = int(input())

# 인접리스트 생성
edge = [[] for _ in range(V+1)]
    
# 방문여부 체크 리스트 생성
chk = [False] * (V+1)

# 결과값 변수 생성
rs = 0

# a와b를 연결하는 간선 비용c 입력
for _ in range(E):
    a, b, c = map(int, input().split())
    #무조건 비용이 앞에오게(heap구조상)해서 인접리스트에 입력
    edge[a].append([c,b])
    edge[b].append([c,a])
    
heap = [[0,1]]

while heap:
    w, each_node = heapq.heappop(heap)
    if chk[each_node] == False:
        chk[each_node] = True
        rs += w
        
        for next_edge in edge[each_node]:
            if chk[next_edge[1]] == False:
                heapq.heappush(heap, next_edge)

print(rs)
    
    
    