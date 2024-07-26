# 1. 아이디어
# 백트래킹 이용, for 돌면서 숫자선택(이때 방문여부체크)
# 재귀함수에서 M개 선택할경우 프린트
# 2. 시간복잡도
# 중복 불가능 --> N은 10까지 가능

# import sys
# input = sys.stdin.readline

# N, M = map(int,input().split())
# result = []
# chk = [False] * (N+1)

# def recur(num):
#     if num == M:
#         print(' '.join(map(str, result)))
#         return
    
#     for i in range(1, N+1):
#         if chk[i] == False:
#             chk[i] = True
#             result.append(i)
#             recur(num + 1)
#             chk[i] = False
#             result.pop()
    
# recur(0)

import sys
input = sys.stdin.readline

n, m = map(int,input().split())
chk = [False] * (n+1) 
result = []

def recur(num):
    if num == 2:
        print(' '.join(map(str, result)))    
    for i in range(1,n+1):
        if chk[i] == False:
            chk[i] == True
            result.append(i)
            recur(num+1)
            chk[i] = False
            result.pop()
recur(0)