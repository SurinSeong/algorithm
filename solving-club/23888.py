import sys

sys.stdin = open('./input/input_23888.txt', 'r')

# 2진수를 10진수로
"""
- 0, 1로 이루어진 1차 배열
- 7개 byte를 묶어서 10진수로 출력하기
"""
def bin_to_dec(bin_num):
    idx = 0
    dec_num = 0
    for n in bin_num[::-1]:
        if n == '1':
            dec_num += 2**idx
        idx += 1

    return str(dec_num)


# 테스트 케이스 수
T = int(input())

for tc in range(1, T+1):
    # 비트 문자열의 입력 개수
    N = int(input())
    # 입력 10개의 비트 문자열이 N개씩 주어짐. (이어져있는 데이터로 간주하기)
    total_bin_str = ''
    for _ in range(N):
        total_bin_str += input().strip()

    answer = []

    # 10진수 변환
    for i in range(10):
        binary_number = total_bin_str[i*7:(i+1)*7]
        answer.append(bin_to_dec(binary_number))

    print(f'#{tc} {" ".join(answer)}')