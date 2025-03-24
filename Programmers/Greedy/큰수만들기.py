def solution(number, k):
    answer = ''
    
    stack = []
    for num in number:
        while k>0 and len(stack)!=0 and num > stack[-1]:
            stack.pop()
            k -= 1
        stack.append(num)
    
    if k > 0:
        stack = stack[:-k]
        
    answer = ''.join(stack)
    
    return answer

# 스택 사용해서 큰수를 만들기

# 스택에 들어올 현재 숫자가 직접에 들어와있는 숫자보다 크면, 직전 숫자 삭제(pop)후 삽입

# 위 경우아니면 그냥 삽입

# k 갯수 고려: 삭제시마다 k 1씩 빼주고, 남은 k 있으면 뒤에서 남은것만큼 삭제