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
   '0001101' : 0,
   '0011001' : 1,
   '0010011' : 2,
   '0111101' : 3,
   '0100011' : 4,
   '0110001' : 5,
   '0101111' : 6,
   '0111011' : 7,
   '0110111' : 8,
   '0001011' : 9
}

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

    # 일의 자리로 변환한 암호 넣는 리스트
    p_list = []

    # 암호의 시작 행을 찾기
    for i in range(N):
        if '1' in password[i]:
            # 시작 행 뒤에서 1을 찾기
            for j, n in enumerate(password[i][::-1], 1):
                if n == '1':
                    last_col = M - j + 1
                    start_col = last_col - 56

                    for idx in range(start_col, last_col, 7):    # 비트 쪼개서 확인하기
                        binary_number = ''.join(password[i][idx:idx + 7])
                        p_list.append(code_dic[binary_number])

                    break    # 변환 암호 다 넣고 끝내기
            break

    # 암호 검사
    answer = check_password(p_list)

    print(f'#{tc} {answer}')
