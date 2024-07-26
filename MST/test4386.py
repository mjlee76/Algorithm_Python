# # 1. 아이디어
# # - 유클리디안 거리 공식을 이용해 
# # - 2차원상의 별들간의 거리를 구하는 함수 생성
# # - 별들 간의 거리를 구하여  MST 이용
# # - 간선을 인접리스트에 넣기
# # - heap에 시작점 넣기
# # - 힙이 빌때까지 다음작업 반복
# #     - 힙의 최소값 꺼내서, 해당 노드 방문하지 않았으면
# #         - 방문 표시, 결과값 추가, 연결된 간선들 힙에 넣기

# import sys
# import math
# input = sys.stdin.readline

# V = int(input())

# # 별의 좌표를 넣을 인접리스트 생성
# vertex = [[] for _ in range(V+1)]

# # 별간의 노드와 간선정보를 입력할 인접리스트 생성
# edge = [[] for _ in range(V+1)]

# star_num = []

# for i in range(1, V+1):
#     a, b = map(float, input().split())
#     star_num.append(i)
#     vertex[i].append([a,b])

# for j in range(V*(V-1)//2):
#     edge[j].append([])
    
# def euclidean_distance(vertex[a],vertex[b]):
#     return math.sqrt((vertex[b][0][0]-vertex[a][0][0])**2 + (vertex[b][0][1]-vertex[a][0][1])**2)
        
    