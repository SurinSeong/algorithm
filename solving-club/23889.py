import sys

sys.stdin = open('./input/input_23889.txt', 'r')

"""
[16진수를 10진수로 변환]
- 먼저 16진수를 4자리의 이진수로 변환하기
- 앞에서 7bit 씩 묶어서 십진수로 변환하기
"""
hex_dic = {
    'A': 10,
    'B': 11,
    'C': 12,
    'D': 13,
    'E': 14,
    'F': 15
}

# 16진수를 10진수로 바꿨다가 4자리 2진수로 바꿔줬음
def hex_to_bin(h):
    d = hex_dic.get(h)

    if d is None:    # d를 찾지 못했다면
        d = int(h)

    binary_number = [0]*4    # 4자리수 이진수로 변환하기 위해
    idx = 0
    while d > 0:
        remain = d % 2
        binary_number[idx] = remain
        idx += 1
        d //= 2

    return ''.join(map(str, binary_number[::-1]))    # 뒤집어서 반환

# 2진수를 10진수로 바꿔주기
def change_to_dec(b):
    dec_num = 0
    idx = 0
    for bi in b[::-1]:
        if bi == '1':
            dec_num += 2**idx
        idx += 1

    return dec_num


# 테스트 케이스 개수
T = int(input())

for tc in range(1, T+1):
    # 16진수 배열
    hex_numbers = input()

    bin_numbers = ''
    for hex_num in hex_numbers:
        bin_numbers += hex_to_bin(hex_num)

    dec_numbers = []
    for i in range(0, len(bin_numbers), 7):
        si, ei = i, i+7
        if ei > len(bin_numbers):    # 7자리까지 있는지 확인하기
            ei = len(bin_numbers)

        bin_num = bin_numbers[si:ei]
        dec_numbers.append(change_to_dec(bin_num))

    print(f'#{tc} {" ".join(map(str, dec_numbers))}')
