"""
[도전]
비트 연산 문제 풀어보기
SWEA 10726. 이진수 표현
- 정수 N, M이 주어질 때, M의 이진수 표현의 마지막 N 비트가 모두 1로 켜져 있는지 아닌지를 판별하여 출력
- 모두 켜져있다면 ON, 아니면 OFF
"""
# M의 우측 N개를 확인할 예정
# 방법 1
def solution1():
    target = M
    for _ in range(N):
        if target & 0x1 == 0:    # 가장 우측 비트가 1인지 체크 (0x1, 0b1, 1 다 사용 가능함. 하지만 0x1은 비트 연산이라는 것을 명시하기 위해 사용한다.)
            return False
        target = target >> 1    # 이진수를 뒤에서부터 확인
    return True

# 방법 2
def solution2():
    # N개의 1을 구함
    mask = (1 << N) - 1
    result = ((M & mask) == mask)
    return result


# 테스트 케이스
T = int(input())

for tc in range(1, T+1):
    # 마지막부터 켜져있어야 할 비트 수, M
    N, M = map(int, input().split())

    answer = solution1()
    # answer = solution2()

    print(f'#{tc} {answer}')