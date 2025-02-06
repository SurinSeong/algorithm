# Baby-gin
"""
10
456790
323123
789789
345345
112233
564564
987987
231234
675678
111222
"""

# 테스트 케이스
T = int(input())

for t in range(1, T+1):
    # num 입력 받기
    num = int(input())

    # count 리스트 설정
    count = [0] * 12

    # count 리스트에 각 자리 수의 개수 넣어주기
    for _ in range(6):
        count[num % 10] += 1
        num //= 10

    i = 0
    tri = run = 0
    # 반복문 이용 - 인덱스 0-9까지
    while i < 10:
        # 1. tri 확인하기
        if count[i] >= 3:
            count[i] -= 3
            tri += 1
            continue

        # 2. run 확인하기
        if (count[i] >= 1) and (count[i+1] >= 1) and (count[i+2] >= 1):
            count[i] -= 1
            count[i+1] -= 1
            count[i+2] -= 1
            run += 1
            continue

        # tri, run 조건 둘다 만족하지 못하면 인덱스 이동
        i += 1

    # baby-gin 인지 판단
    if tri + run >= 2:
        print(f'{t} Baby-Gin')
    else:
        print(f'{t} Fail')
