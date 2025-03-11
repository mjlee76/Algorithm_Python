def solution(clothes):
    answer = 1
    closet = {}
    for item, type in clothes:
        if type not in closet.keys():
            closet[type] = [item]
        else:
            closet[type] += [item]
            
    # for keys,values in closet.items():
    #     answer *= (len(values)+1)
        
    for values in closet.values():
        answer *= (len(values)+1)
    
    return answer-1

# 총 착용가능한 착장 가짓 수, 같은 종류의 의상은 하나만 착용가능, 하나만 착용도 가능, 아무것도 없으면 안됨

# 모자 m개, 상의n개 일때 총 가짓 수 -> (m+1)(n+1) -> mn:둘다 착용, m:모자만 착용, n:상의만 착용, 1: 둘다 착용안함

# 위 식을 구현하면 됨

# clothes 2차원 배열의 예시 -> [["yellow_hat", "headgear"], ["green_turban", "headgear"]], ["blue_sunglasses", "eyewear"]

# clothes 2차원 배열을 item(옷->값), type(종류->키)로 돌면서 closet 딕셔너리에 closet[type] = [item]식으로 종류별 옷을 담음

# print(closet) => {'headgear': ['yellow_hat', 'green_turban'], 'eyewear': ['blue_sunglasses']}

# closet.values():아이템만 -> 이걸 for문 돌려서 아이템 갯수+1 을 전부 곱해서 answer에 담음

# 아무것도 착용안한 가짓 수 1을 빼줌