def solution(brown, yellow):
    answer = []
    
    size = brown + yellow
    
    for i in range (3, size//2):
        if size % i == 0:
            if (i-2) * ((size//i)-2) == yellow:
                answer.append(size//i)
                answer.append(i)
                break
                
    answer.sort(reverse=True)
    
    return answer

# 갈색 + 노란색 = 전체 사이즈

# 전체 사이즈를 3부터 나눠서 나머지가 0일때 가로 세로를 구함

# 구한 가로와 세로를 이용해: (가로-2) * (세로-2) = 노란색크기 인것을 리스트에 넣고

# 내림차순 정렬