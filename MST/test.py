import random

N = int(input("세트 수를 입력하세요 : "))

rand = list(range(1, 46))
result=[]
for i in range(1, N+1):
    numbers = random.sample(rand, 6)
    numbers.sort()
    result.append(numbers)
    
print(f"<로또 당첨 예상번호 세트>")
for i in range(N): 
    print(f"세트{i+1} : {' '.join(map(str, result[i]))}")

