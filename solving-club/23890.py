import sys

sys.stdin = open('./input/input_23890.txt', 'r')

"""
[16진수 암호 비트 패턴 출력]
- 일단 먼저 16진수를 이진수로 변환하고
- 암호를 찾기 (뒤에서 부터 찾기)
"""
# 16진수를 2진수로
hex_dict = {
    'A': 10,
    'B': 11,
    'C': 12,
    'D': 13,
    'E': 14,
    'F': 15
}

# 16진수를 2진수로 변환
def change_to_bin(h):
    # 1. 10진수로 변환
    d = hex_dict.get(h)
    if d is None:
        d = int(h)

    # 2. 4자리 2진수로 변환
    b = [0] * 4
    for i in range(4):
        if d < 0:    # 0보다 작아지면 끝낸다
            break

        remain = d % 2
        b[i] = remain
        d //= 2

    # 반대로 돌려서 반환
    return ''.join(map(str, b[::-1]))

# 암호 비트 패턴
code_pattern = {
    '001101': 0,
    '010011': 1,
    '111011': 2,
    '110001': 3,
    '100011': 4,
    '110111': 5,
    '001011': 6,
    '111101': 7,
    '011001': 8,
    '101111': 9
}

# 1 찾는 함수
def find_one(b_string):
    ei = len(b_string)-1    # 가장 마지막 인덱스
    while True:
        # 종료조건
        if b_string[ei] == '1':
            ei += 1
            si = ei - 6
            return si, ei

        ei -= 1


# 테스트 케이스 개수
T = int(input())

for tc in range(1, T+1):
    # 16진수
    hex_numbers = input().strip()

    # 1. 4자리 2진수 배열 만들기
    bin_numbers = ''
    for h in hex_numbers:
        bin_numbers += change_to_bin(h)

    # 2. 암호 찾기
    codes = []

    while '1' in bin_numbers:

        if len(bin_numbers) < 6:    # 남은 이진수의 길이가 7보다 작으면 확인할 필요 없음.
            break

        s, e = find_one(bin_numbers)    # 시작, 끝 인덱스 찾기

        if s < 0:    # 시작 인덱스가 0보다 작으면 암호 찾기 종료
            break

        codes.append(code_pattern[bin_numbers[s:e]])    # 찾은 숫자 넣기
        bin_numbers = bin_numbers[:s]    # 이진수 배열 업데이트

    print(f'#{tc} {" ".join(map(str, codes[::-1]))}')