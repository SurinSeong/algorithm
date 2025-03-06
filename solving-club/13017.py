"""
[이진수2]
- 0보다 크고 1 미만인 십진수 N을 이진수로 바꾼다.
- N : 십진수
- N을 소수점 아래 12자리 이내인 이진수로 표시할 수 있으면 0.를 제외한 나머지 숫자 출력
- 13자리 이상이 필요하면 overflow를 출력한다.
"""
import sys

sys.stdin = open('./input/input_13017.txt', 'r')

# 함수 만들기
def dec_to_bin_minus(num):
    bin_num = ''
    idx = -1
    result = 'overflow'

    # 12자리까지 확인하기
    while idx > -13:
        if num - 2**idx > 0:    # 결과가 양수면
            bin_num += '1'    # 1 추가
            num -= 2**idx   # 업데이트
            idx -= 1    # 제곱근 업데이트

        elif num - 2**idx == 0:    # 0이면
            bin_num += '1'    # 1 추가해주고
            return bin_num    # 결과 반환

        else:
            bin_num += '0'    # 음수면
            idx -= 1    # 제곱근 업데이트

    return result

# 테스트 케이스 개수
T = int(input())

for tc in range(1, T+1):
    # 소수점 아래가 12자리 이내인 N
    N = float(input())

    answer = dec_to_bin_minus(N)

    print(f'#{tc} {answer}')

