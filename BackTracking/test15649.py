# 1. 아이디어
# - 백트래킹 재귀함수 안에서, for 돌면서 숫자 선택(이때 방문 여부 확인)
# - 재귀함수에서 M개를 선택할경우 print

# 2. 시간복잡도
# N! : 중복 불가능, N=10 까지 가능(N은 8 까지라 가능)

# 3. 자료구조
# 방문 여부 체크 : bool[]
# 결과값 저장 : int[]

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
result = []
chk = [False] * (N+1) # 첫번째값을 chk[0]이 아닌 chk[1]로 접근하기위해 N+1

def recur(num):
    if num == M: #원하는 갯수를 다 뽑은 경우 -> 출력
        print(' '.join(map(str, result))) 
        # map으로 result를 string으로 바꾼다음 
        # 값사이에 공백넣어서 join
        return # 재귀함수 종료시점 중요!!
    
    for i in range(1, N+1):
        if chk[i] == False:
            chk[i] = True
            result.append(i)
            recur(num + 1)
            #재귀함수 호출후 num==M이여서 return되면
            
            #다시 chk[i]의 방문을 초기화해주고
            chk[i] = False
            
            #마지막 추가된값을 빼줘야함
            result.pop()
            
            #이유는 [1,2]가 출력되고 
            # 다시 [1]로 돌아와 [1,3]을 출력해야하기 때문

recur(0)
