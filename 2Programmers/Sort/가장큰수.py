def solution(numbers):
    answer = ''
    p = []
    p.extend(permutations(numbers, len(numbers)))
    
    result = []
    for tuple in p:
        result.append(int(''.join(map(str, tuple))))
    
    result.sort()
    
    return str(result[-1])

# 이렇게 하면 모든 numbers를 순열 처리하므로 시간복잡도가 매우 커짐 -> 효율성 검사 실패

def solution(numbers):
    answer = ''
    
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x:x*3, reverse = True)
    
    for num in numbers:
        answer += num
        
    return str(int(answer))

# numbers의 원소는 0부터 1000까지의 수가 들어감

# number의 원소가 [221,2,10]로 주어진다 가정했을 때 가장 큰 수는 '2'+'221'+'10' -> 222110 이 되야함

# 따라서 
# 1. 문자열로 바꿔서 합침 
# 2. [2, 221, 10]으로 정렬 가능해야함

# 여기서 2번을 수행하려면 숫자를 3번 합쳐주면 221221221, 222, 10 이 됨
# 이러혐 221 보다 222가 사전적 순서로 큼 -> numbers가 0~1000까지 이므로 세번은 합쳐줘야 원하는 정렬 가능
# 예를 들어 numbers의 원소가 0~100이면 두번만 합쳐주면 가능

# key = lambda x:x*3 으로 세번 합쳐준 뒤 정렬(내림차순으로)

# 모든 원소를 앞에서부터 차례로 합치면 가장 큰 수 완성

# return값에 str(int(answer)) 한 이유는 000같은 문자열이 0으로 표현되야 하므로 int로 바꿨다가 str로 출력