import sys

sys.stdin = open('./input/input_13016.txt', 'r')

"""
[이진수]
- 16진수 1자리 = 2진수 4자리
- N자리 16진수 >> 4자리 2진수로 표현하기!
- 2진수의 앞자리 0도 표시한다.
"""
# 10진수를 2진수로
def dec_to_bin(number):
    bin_number = ['0']*4
    idx = 0
    while number > 0:
        remain = str(number % 2)
        bin_number[idx] = remain
        number //= 2
        idx += 1

    return ''.join(bin_number[::-1])


# 2진수로 바꾸기 (함수 이용)
def hex_to_bin(hex_number):
    # 문자 딕셔너리
    hex_dict = {'A': 10,
                'B': 11,
                'C': 12,
                'D': 13,
                'E': 14,
                'F': 15}

    if hex_number in hex_dict:    # 딕셔너리에 키값이 있다면
        dec_num = hex_dict[hex_number]    # 그 value로 10진수를 설정한다.
    else:
        dec_num = int(hex_number)

    return dec_to_bin(dec_num)    # 10진수를 2진수로 변환


# 테스트 케이스 개수
T = int(input())

for tc in range(1, T+1):
    # 16진수의 자리
    N, hex_num = input().split()

    answer = []
    # 16진수를 돌면서 변환한다.
    for num in hex_num:
        answer.append(hex_to_bin(num))

    print(f'#{tc} {"".join(answer)}')