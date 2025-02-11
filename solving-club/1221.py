# 작은수로 정렬하기
import sys
from pathlib import Path

filename = Path.cwd() / 'solving-club/input/input_1221.txt'
sys.stdin = open(filename, 'r')

# 테스트 케이스
T = int(input())

for _ in range(T):
    t, N = map(str, input().split())
    print(t)
    number_list = input().split()

    # value가 없는 딕셔너리 만들기
    numbers = {'ZRO': 0, 'ONE': 0, 'TWO': 0, 'THR': 0, 'FOR': 0, 'FIV': 0, 'SIX': 0, 'SVN': 0, 'EGT': 0, 'NIN': 0}

    # 각 단어의 숫자 세기
    for number in number_list:
        numbers[number] = numbers.get(number) + 1
    # 딕셔너리에서 순서대로 print 하기
    for number in numbers:
        for i in range(numbers[number]):
            print(number, end=' ')
    print()