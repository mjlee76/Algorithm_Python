def solution(s):
    
    stack = []
    
    for char in s:
        if char == '(':
            stack.append(char)
            
        else:
            if not stack:
                return False
            else:
                stack.pop()
                
    return not stack


# s는 괄호'(',')'로 구성된 문자열이다.

# s가 괄호가 잘 닫혀있으면 true 아니면 false를 반환하는 문제

# 스택을 사용함(LIFO: 후입선출)

# 처음이 '(' 이거면 stack에 추가

# 처음이 ')' 이거면 -> stack이 비어있다면 false, 비어있지 않다면 쌍이 맞는것이므로 stack에 남아있던 '('를 pop()

# 스택에는 애초에 ')'는 들어가지 않음

# 예시
# s = '((()))'
# 1: ['(']
# 2: ['(', '(']
# 3: ['(', '(', '(']
# 4: ['(', '(']
# 5: ['(']
# 6: []