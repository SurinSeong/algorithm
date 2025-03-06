def dec_to_hex(target):
    hex_digit = '0123456789ABCDEF'    # 미리 설정해준다.
    hex_number = ""    # 결과 넣는 문자열

    while target > 0:
        remain = target % 16
        hex_number = hex_digit[remain] + hex_number
        target //= 16

    return hex_number

target = 256
print(dec_to_hex(target))