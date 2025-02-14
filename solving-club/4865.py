# str1에 포함된 글자들이 str2에 몇개씩 들어있는지 찾기
# 가장 많은 글자의 개수 출력
import sys
from pathlib import Path

filename = Path.cwd() / 'solving-club/input/input_4865.txt'
sys.stdin = open(filename, 'r')

# 테스트 케이스 개수
T = int(input())

for t in range(1, T+1):
    str1 = list(input())
    str2 = input()
    # str1의 글자를 하나씩만 있도록 만들기
    str1 = list(set(str1))
    # 가장 많은 글자의 개수를 0이라고 가정
    max_num = 0
    # str2를 반복문으로 돌며 개수 세기
    for alpha in str1:
        current_num = 0
        for c in str2:
            if c == alpha:
                current_num += 1
        max_num = max(max_num, current_num)

    print(f'#{t} {max_num}')