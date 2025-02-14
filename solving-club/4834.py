# 숫자 카드
# N장의 카드 -> 0~9
# 가장 많은 카드에 적힌 숫자와 카드가 몇장일까?
# 카드 장수가 같을 때는 적힌 숫자가 큰 쪽을 출력하기

# 테스트 케이스 수
T = int(input())

# T번 반복
for t in range(1, T+1):
    # 카드의 개수
    N = int(input())
    # 숫자들
    numbers = int(input())
    # 숫자 개수 세기
    # count 리스트 만들기
    count = [0]*10  # 0-9

    for _ in range(N):
        count[numbers % 10] += 1
        numbers //= 10

    # count 에서 가장 큰 인덱스 구하기
    max_idx = 0

    for i in range(1, 10):
        if count[max_idx] <= count[i]:
            max_idx = i

    print(f'#{t} {max_idx} {count[max_idx]}')