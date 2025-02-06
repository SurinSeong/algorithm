# 간단한 소인수분해

# 테스트 케이스
T = int(input())

for t in range(1, T+1):
    print(f'#{t}', end=' ')
    # N
    N = int(input())
    # 각 숫자의 지수
    for divisor in [2, 3, 5, 7, 11]:
        count = 0
        while True:
            if N % divisor == 0:
                count += 1
                N //= divisor
            else:
                break

        if divisor != 11:
            print(f'{count}', end=' ')
        else:
            print(f'{count}')