# 1.아이디어
# - 배열이용, (남자 & 여자) 통해 종료시 다음사람으로 이동
# - 배열 출력
# - (남): if문으로 i가 num의 배수인것 찾기
#  if i%num = 0
# - (여): 

import sys
input = sys.stdin.readline

N = int(input())
switch = [-1] + list(map(int, input().split()))
students = int(input())

def change(num):
    if switch[num] == 0:
        switch[num] = 1
    else:
        switch[num] = 0
    return

for _ in range(students):
    sex, num = map(int, input().split())
    #남자
    if sex == 1:
        for i in range(1, N+1):
            if i % num == 0:
                change(i)
    #여자
    else:
        change(num)
        for k in range(N//2):
            if num - k < 1 or num + k > N:
                break
            if switch[num-k] == switch[num+k]:
                change(num-k)
                change(num+k)
            else:
                break

for i in range(1, N+1):
    print(switch[i], end = " ")
    if i % 20 == 0:
        print()

                