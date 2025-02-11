# 의석이의 세로로 말해요
# 자석 글자 -> 'A'~'Z', 'a'~'z', 0~9
# 가로로 붙인 글자를 세로로 읽기
import sys
from pathlib import Path

filename = Path.cwd() / 'solving-club/input/input_5356.txt'
sys.stdin = open(filename, 'r')

# 테스트 케이스 개수
T = int(input())

for t in range(1, T+1):
    words_matrix = [list(input()) for _ in range(5)]
    max_len = max(map(len, words_matrix))
    print(f'#{t}', end=' ')
    # 가장 긴 길이만큼 반복
    for j in range(max_len):
        for i in range(5):
            if max_len > len(words_matrix[i]):
                words_matrix[i] += ['']*(max_len-len(words_matrix))
            print(words_matrix[i][j], end='')

    print()