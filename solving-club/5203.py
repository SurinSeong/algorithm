"""
[베이비진]
- 0 ~ 9
- 6개 골랐을 때, 연속인 숫자가 3개 이상이면 run, 같은 숫자가 3개 이상이면 triplet
"""
def is_run(arr):
    for i in range(8):
        if (arr[i] >= 1) and (arr[i+1] >= 1) and (arr[i+2] >= 1):
            return True
    return False


def is_triplet(arr):
    for i in range(10):
        if arr[i] >= 3:
            return True
    return False

def is_win(arr):
    if sum(arr) < 3:
        return False

    if is_run(arr):
        return True

    if is_triplet(arr):
        return True

    return False


# 테스트 케이스 개수
T = int(input())

for tc in range(1, T+1):
    cards = list(map(int, input().split()))
    player1, player2 = [0]*10, [0]*10
    winner = 0
    # 교대로 가져간다.
    for i in range(6):
        player1[cards[i*2]] += 1
        player2[cards[i*2+1]] += 1

        state1 = is_win(player1)
        state2 = is_win(player2)

        if state1:
            winner = 1
            break

        if state2:
            winner = 2
            break

    print(f'#{tc} {winner}')





