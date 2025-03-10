"""
[국민셔플]
- 하위의 37%의 카드수를 위로 올리는 오버핸드 셔플
- 카드를 교차로 섞는 퍼펙트 셔플

- 초기 상태의 카드 정보 >> T번의 셔플 이후 결과를 알려주는 프로그램
- 한 번의 셔플 : 오버핸드 셔플 1회 + 퍼펙트 셔플 1회
- N장의 카드를 T번의 셔플 set 이후 결과 출력

[초기상태]
- 1~N번의 카드 : 순차적

[오버핸드]
- 37%의 정수부에 해당하는 카드를 상위로 올림.

[퍼펙트]
- 50%의 하위 카드를 상위에 있는 카드와 교차로
"""
def overhand(arr):
    # 하위 37%를 앞으로 옮겨준다.
    low_37 = int(N * 0.63)+1     # 뒤에서부터의 인덱스

    new_arr = arr[low_37:]+arr[:low_37]

    return new_arr


def perfect(arr):
    # 새로 정렬할 리스트
    perfect_shuffle = [0] * N

    part1 = arr[:(N - 1) // 2 + 1]
    part2 = arr[(N - 1) // 2 + 1:]
    for i in range(N // 2):
        perfect_shuffle[i * 2] = part1[i]
        perfect_shuffle[i * 2 + 1] = part2[i]

    if N % 2:
        perfect_shuffle[-1] = part1[-1]

    return perfect_shuffle


def shuffle(s, arr):
    for _ in range(s):
        arr = perfect(overhand(arr))

    return arr


# 테스트 케이스 개수
T = int(input())

for tc in range(1, T+1):
    # 카드의 개수, 셔플 횟수
    N, S = map(int, input().split())

    # 리스트로 받아둔다.
    cards = [i for i in range(1, N+1)]

    answer = shuffle(S, cards)

    print(f'#{tc} {" ".join(map(str, answer))}')