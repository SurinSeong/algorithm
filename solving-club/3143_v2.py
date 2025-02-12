# 가장 빠른 문자열 타이핑
# 속도를 조금 더 높이기 위해 어떤 문자열 B가 저장되어 있어서 키를 한번 누른 것으로 B전체를 타이핑 가능
import sys
from pathlib import Path

filename = Path.cwd() / 'solving-club/input/input_3143.txt'
sys.stdin = open(filename, 'r', encoding='utf-8')


# 완전 탐색
def brute_force(t, p):
    n, m = len(t), len(p)
    i = j = 0
    total = 0
    while i < n:
        if t[i] != p[j]:
            i = i - j + 1
            j = 0
        else:
            i += 1
            j += 1
        if j == m:
            total += 1
            i = i - j + 1
            j = 0
    return total

# KMP 알고리즘
def kmp(t, p):
    n, m = len(t), len(p)
    # 전처리
    lps = [0]*(m+1)
    lps[0] = -1
    j = 0
    for i in range(1, m):
        lps[i] = j
        if t[i-1] != t[i]:
            j = 0
        else:
            j += 1
    lps[m] = j
    # 찾기
    i = j = 0
    cnt = 0
    while i < n and j <= m:
        if (j == -1) or t[i] == p[j]:
            i += 1
            j += 1
        else:
            j = lps[j]
        if j == m:
            cnt += 1
            j = lps[j]
    return cnt


# 테스트 케이스
T = int(input())

for tc in range(1, T+1):
    A, B = input().split()

    cnt = kmp(A, B)
    cnt += (len(A)-len(B)*cnt)

    print(f'#{tc} {cnt}')