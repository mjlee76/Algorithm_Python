def solution(answers):
    result = []
    supo1 = [1,2,3,4,5]
    supo2 = [2,1,2,3,2,4,2,5]
    supo3 = [3,3,1,1,2,2,4,4,5,5]
    
    count1 = 0
    for i in range (len(answers)):
        k = i % 5
        if answers[i] == supo1[k]:
            count1 += 1
    count2 = 0
    for i in range (len(answers)):
        k = i % 8
        if answers[i] == supo2[k]:
            count2 += 1
    count3 = 0
    for i in range (len(answers)):
        k = i % 10
        if answers[i] == supo3[k]:
            count3 += 1
            
    max_count = max(count1,count2,count3)
    if count1 == max_count:
        result.append(1)
    if count2 == max_count:
        result.append(2)
    if count3 == max_count:
        result.append(3)
        
    return result


    # 완전탐색
    # 모의고사 찍는 패턴 1,2,3 중 더 answers(답)을 많이 맞추는 값 리턴