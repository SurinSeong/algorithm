"""
[단순 2진 암호코드]
- 암호코드 : 8개의 숫자
- 숫자 하나는 7개의 비트로 암호화
    - 암호 코드의 가로 길이 : 56

[암호 코드]
- 홀수 자리의 합 *3 + 짝수 자리의 합 = 10의 배수
- 암호 코드 정보가 포함된 2차원 배열을 입력으로 받아 올바른 암호코드인지 판별하기
"""
import sys

sys.stdin = open('./input/input_1240.txt', 'r')

code_dic = {
               (3, 2, 1, 1) : 0,
               (2, 2, 2, 1) : 1,
               (2, 1, 2, 2) : 2,
               (1, 4, 1, 1) : 3,
               (1, 1, 3, 2) : 4,
               (1, 2, 3, 1) : 5,
               (1, 1, 1, 4) : 6,
               (1, 3, 1, 2) : 7,
               (1, 2, 1, 3) : 8,
               (3, 1, 1, 2) : 9
            }

# 이진을 십진으로
def code_to_dec(code):
    orders = [1]*4
    idx = 0
    first = code[0]
    for c in code[1:]:
        if c == first:
            orders[idx] += 1
        else:
            first = c
            idx += 1

    return code_dic[tuple(orders)]


# 암호 검사
def check_password(arr):
    odd_nums, even_nums = 0, 0
    for i, p in enumerate(arr, 1):
        if i % 2:    # 홀수이면
            odd_nums += p
        else:
            even_nums += p

    total = odd_nums*3 + even_nums
    if total % 10 == 0:
        return odd_nums+even_nums
    else:
        return 0


# 테스트 케이스 개수
T = int(input())

for tc in range(1, T+1):
    # 세로, 가로
    N, M = map(int, input().split())
    # 배열 받기
    password = [list(input()) for _ in range(N)]

    # 암호의 시작 행을 찾기
    for i in range(N):
        if '1' in password[i]:
            start_row = i
            break

    # 시작 행 뒤에서 1을 찾기
    for j, n in enumerate(password[start_row][::-1], 1):
        if n == '1':
            last_col = M-j+1
            start_col = last_col - 56
            break

    p_list = []
    for idx in range(start_col, last_col, 7):
        binary_number = password[start_row][idx:idx+7]
        p_list.append(code_to_dec(binary_number))

    # 암호 검사
    answer = check_password(p_list)

    print(f'#{tc} {answer}')
