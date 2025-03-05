import sys
from pathlib import Path

filename = Path.cwd() / 'solving-club/input/input_14510.txt'
sys.stdin = open(filename, 'r')
"""
[나무의 키]
- 홀수 +1, 짝수 +2
- '모든' 나무의 키가 처음에 가장 키가 컸던 나무와 같아지도록 할 수 있는 최소 날짜의 수
- 물을 주지 않을 수 있음.

[조건]
- 나무 개수 : 2 <= <= 100
- 초기 높이 : 1 <= <= 120
"""
# 나머지 찾는 함수
def remain_one_or_two():
    global one, two, answer

    for gap in gaps:
        answer += (gap // 3) * 2
        if gap % 3 == 1:    # 3으로 나눠떨어지지 않으면
            one += 1
        elif gap % 3 == 2:
            two += 1


# 1-2 쌍 찾는 함수
def find_pairs():
    global one, two, answer

    if one > two:
        one -= two
        answer += (two*2)
        two = 0
    elif one < two:
        two -= one
        answer += (one*2)
        one = 0
    else:
        answer += (one*2)
        one, two = 0, 0

# 남은 1 또는 2 계산해주기
def final_days(one, two):
    global answer

    if one == 0 and two == 0:    # 둘 다 0이라면
        return answer

    if two == 0:    # 1이 남았다면
        answer += (2*one-1)
        return answer

    if one == 0:    # 2가 남았다면
        if two == 1:    # 2가 하나만 남았다면
            answer += 2
            return answer
        else:    # 2가 여러개 남았다면
            while True:
                two -= 1
                one += 2
                if abs(two-one) > 1:
                    continue
                else:
                    answer += (abs(two-one)*2)
                    if two > one:
                        answer += 2
                        return answer
                    elif two < one:
                        answer += 1
                        return answer
                    else:
                        return answer


# 테스트 케이스 수
T = int(input())

for tc in range(1, T+1):
    # 나무의 개수
    N = int(input())
    # 나무들의 높이
    trees = list(map(int, input().split()))

    # 처음 가장 키가 큰 나무
    max_h = max(trees)

    # 가장 키가 큰 나무에서 다 뺀 차이를 넣는 리스트
    gaps = [max_h - tree for tree in trees if tree != max_h]

    # 나머지 담는 리스트
    answer, one, two = 0, 0, 0

    remain_one_or_two()
    find_pairs()
    final_answer = final_days(one, two)

    print(f'#{tc} {final_answer}')










