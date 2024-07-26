# 1.아이디어
# 수열계산하는 함수 && DFS함수
# 수열에 등장할수있는 가장큰 크기의 check리스트를 만들어(0초기화)
# 값이 등장할시에 +1해줌 ==> 나중에 해당값이 가리키는 check가
# 0이 아니면 그값나오기 전까지의 값을 출력
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
check = [0] * 236197  # 236197은 나올수있는 최대수

iteration = 1  # iteration은 check[n]값의 순서를 뜻한다(처음은 1부터 시작이니 1로 초기화)

def cal(a, b):
    result = 0
    for i in str(a):
        result += pow(int(i), b)
    return result

def dfs(n, m, iteration, check):
    if check[n] != 0:
        return check[n] - 1
    
    check[n] = iteration
    iteration += 1
    result = cal(n, m)
    return dfs(result, m, iteration, check)


print(dfs(n, m, iteration, check))
