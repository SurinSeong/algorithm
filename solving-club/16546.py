# Baby-gin 실습
# 테스트 케이스
T = int(input())

for t in range(1, T+1):
    # 6장의 카드 숫자
    cards = int(input())
    # count 리스트에서 숫자 세기
    count = [0] * 12
    for _ in range(6):
        # 각 자리수를 인덱스로 해서 개수 계산
        count[cards % 10] += 1
        cards //= 10

    total = 0
    i = 0

    while i < 10 :
        if count[i] >= 3:
            count[i] -= 3
            total += 1
            continue
        if (count[i] >= 1) and (count[i+1] >= 1) and (count[i+2] >= 1):
            count[i] -= 1
            count[i+1] -= 1
            count[i+2] -= 1
            total += 1
            continue
        i += 1

    if total >= 2:
        print(f'#{t} true')
    else:
        print(f'#{t} false')