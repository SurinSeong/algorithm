# 가장 빠른 문자열 타이핑
# 속도를 조금 더 높이기 위해 어떤 문자열 B가 저장되어 있어서 키를 한번 누른 것으로 B전체를 타이핑 가능
import sys
from pathlib import Path

filename = Path.cwd() / 'solving-club/input/input_3143.txt'
sys.stdin = open(filename, 'r', encoding='utf-8')


# 테스트 케이스
T = int(input())

for tc in range(1, T+1):
    A, B = input().split()
    len_b = len(B)
    new_A = A.replace(B, '')
    cnt = len(new_A) + (len(A) - len(new_A))//len_b

    print(f'#{tc} {cnt}')