# 1. 아이디어
# - 백트래킹 재귀함수 안에서 for문 돌면서 사용

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
result = []

def recur(start, num):
    if num == M: 
        print(' '.join(map(str, result))) 
        return # 재귀함수 종료시점 중요!!
    
    for i in range(start, N+1):
            result.append(i)
            recur(i + 1,num + 1)
        
            result.pop()

recur(1, 0)
