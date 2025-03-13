"""
[도전] 주사위 던지기
- 주사위 눈금 N개를 던져서 나올 수 있는 모든 조합 출력
"""
def get_comb(cnt, start):
    if cnt == r:
        print(comb)
        return

    for i in range(start, N):

        comb.append(dice_numbers[i])
        get_comb(cnt+1, i)
        comb.pop()


dice_numbers = [1, 2, 3, 4, 5, 6]
N = 6
r = 3

comb = []

get_comb(0, 0)