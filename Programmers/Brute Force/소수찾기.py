from itertools import permutations

# 소수 판별 함수 선언
def is_prime(n):
    if n < 2:
        return False
    
    for i in range(2, n//2+1):
        if n % i == 0:
            return False
    
    return True

def solution(numbers):
    answer = 0
    p = []
    result = []
    
    for i in range(1, len(numbers)+1):
        p.extend(permutations(numbers, i))
        
    for k in range(len(p)):
        result.append(int(''.join(p[k])))
    
    print(set(result))
    
    for num in set(result):
        if is_prime(num) == True:
            answer += 1
            
    return answer


# 숫자 조각으로 숫자 만들기 -> 10 과 01 은 다른 숫자가 되야함(순서가 중요) -> 순열(Permutation) 사용 

# set() 함수로 중복 제거

# 소수 찾기 함수 선언: is_prime