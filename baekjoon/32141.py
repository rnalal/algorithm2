#32141번 - 카드 게임
#첫 번째 줄에 상대를 죽이기 위해 사용할 수 있는 카드의 최대 개수를 출력하여라.
#만약 모든 카드를 사용해도 죽일 수 없다면 -1을 출력하여라.

#H = 체력
#N = 공격력 가진 카드 개수
#D = N개 카드의 공격력 di 오름차순
#kill_count = 사용한 카드 개수

N, H = map(int, input().split())
D = list(map(int, input().split()))

kill_count = 0
for damage in D:
    H -= damage
    kill_count += 1
    if H < 0 :
        print(kill_count)
        exit()

print(-1)       

