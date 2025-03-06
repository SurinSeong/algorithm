def bin_to_dec(binary_str):
    decimal_number = 0    # 10진수
    pow = 0    # 각 자리 위치 (지수)

    for digit in binary_str[::-1]:    # 1) 인자로 받은 문자열을 뒤에서부터 진행한다.
        # 2) 각 자리에 맞는 수를 곱하며, 결과에 더한다.
        if digit == '1':    # 1이면 위치 제곱
            decimal_number += 2**pow
        pow += 1    # 위치 이동

    return decimal_number

binary_str = "10010101"
print(bin_to_dec(binary_str))