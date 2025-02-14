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
    # 글자 넣기
    words_matrix = [list(input()) for _ in range(5)]
    # 가장 긴 길이 찾기
    max_len = max(map(len, words_matrix))
    # 테스트 케이스 번호 넣기
    print(f'#{t}', end=' ')
    
    for word in words_matrix:
        if len(word) < max_len:
            word += '*'*(max_len - len(word))
    
    # 전치
    matrix_T = list(map(list, zip(*words_matrix)))
    
    for arr in matrix_T:
        for char in arr:
            if char != '*':
                print(char, end='')
    print()
    