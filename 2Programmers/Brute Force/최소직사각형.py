def solution(sizes):
    
    answer = 0
    w = []
    h = []
    
    for i in range (len(sizes)):
        w.append(max(sizes[i]))
        h.append(min(sizes[i]))
        
    answer = max(w) * max(h)
        
    print(f'w: {w}')
    print(f'h: {h}')
    return answer

# 완전탐색

# sizes: 여러 명함의 가로 세로 사이즈
# 모든 명함을 담지만 가장 크기가 작은 넓이 구하기

# 각 명함을 반복문으로 돌면서 큰값을 w에 넣고 작은값을 h에 넣음

# 가장 큰 w와 가장큰 h를 곱한 값을 return