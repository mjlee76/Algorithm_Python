from itertools import permutations
def solution(k, dungeons):

    p = []
    p.extend(permutations(dungeons, len(dungeons)))
    result = []
    
    #print(p)
    for perm in p:
        count = 0
        condition = k
        for min_con, cost in perm:
            if condition>=min_con:
                condition -= cost
                count += 1
                if condition <= 0:
                    break
        result.append(count)
        
    return max(result)

# 피로도 k 와 [입장 가능한 최소피로도, 소모되는 피로도]의 던전들로 구성된 dungeons 리스트가 주어지고
# 가장 많이 탐험할수 있는 던전갯수를 return -> 던전 입장 순서를 고려해서 최대한 많이 탐험해야함

# 그리디한 방식으로 풀면 -> 입장가능한 최소피로도가 높을수록, 소모되는 피로도가 낮을수록 -> 우선순위가 높아짐
# (최소피로도/소모피로도)를 구해 우선순위로 정렬후 문제 풀면 -> 반례 케이스가 있어서 불가능

# 이건 그냥 완전 탐색이 맞다 -> 왜냐하면 dungeons이 최대 8가지 밖에 없음 -> 순열 이용해 최대 8! 밖에 안됨

# itertools의 permutations이용해서 전체 던전 탐험 방법을 만들어서
# 모든 가짓수별 count를 result에 저장해서
# 가장 큰 result값 출력