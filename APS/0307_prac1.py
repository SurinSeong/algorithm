"""
[연습문제 1]
- 0과 1로 이루어진 1차 배열에서 7개씩 수를 묶어, 10진수로 출력

0000000111100000011000000111100110000110000111100111100111111001100111
"""
def change_to_decimal(binary_number):
    result = 0
    idx = 0
    for n in binary_number[::-1]:    # 뒤에서 부터 반복
        if n == '1':
            result += 2**idx    # 더해주기
        idx += 1    # 자리 업데이트

    return result


bin_N = input()
N = len(bin_N)

number_list = []

for i in range(0, N, 7):
    dec_N = change_to_decimal(bin_N[i:i+7])
    number_list.append(dec_N)

print(' '.join(map(str, number_list)))