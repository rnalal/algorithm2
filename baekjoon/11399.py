#ATM - 11399번

#N = 사람의 수
#P1,P2,P2...Pi = 각 사람이 돈을 인출하는데 걸리는 시간
#sum = 모든 사람이 돈을 인출하는데 걸린 시간들의 합

#각 사람이 돈을 인출하는데 필요한 시간 합의 최솟값을 구하려면
#먼저, 필요한 시간이 적은 순으로 사람들을 정렬한 후 합을 계산하면 됨.

N = int(input()) #입력한 정수를 int로 변환해서 N에 저장
P = list(map(int, input().split()))

result=[] #누적 합을 저장할 리스트 
times = 0 #누적 합을 계산할 변수

P.sort() #P리스트를 오름차순으로 정렬

#리스트 P를 반복하면서, 이전까지의 합을 계산하고 result 리스트에 저장.
for i in P:
    times += i
    result.append(times)

times_sum = sum(result) #result 리스트의 총합
print(times_sum)    
