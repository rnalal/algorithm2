# 타슈 - 30018번

# N = 대여소 개수
# A1, A2, A3, A4, ... , An = 처음 자전거 개수
# B1, B2, B3, B4, ... , Bn = 나중 자전거 개수2
# sum = 자전거 옮긴 횟수

# 나중 자전거 개수(Bn)와 처음 자전거 개수(An)를 같게 하려면 
# Bn > An 인 경우에만 자전거를 옮긴 횟수를 세면 됨.

N = int(input()) #입력한 정수를 int로 변환해서 N에 저장
A = list(map(int, input().split()))
B = list(map(int, input().split()))

total_sum = 0
for i in range(N): #i를 0부터 N-1까지 반복
    if A[i] > B[i]:
        total_sum += A[i] - B[i]
    else:
        pass

print(total_sum)    