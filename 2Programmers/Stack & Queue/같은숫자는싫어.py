def solution(arr):
    result = []
    for num in arr:
        if len(result) == 0 or result[-1] != num:
            result.append(num)
    return result

# arr에 숫자 배열이 주어지는데 여기에서 순서는 유지하고 중복은 제거된 배열을 반환하는 문제

# 스택(LIFO:후입선출)을 이용, result[-1] => 가장 마지막에 들어온 값

# arr 배열을 돌며 num을 result에 append하기 전에

# if 조건으로 result가 비어있거나 마지막값(result[-1])이랑 num이랑 다르면 => append