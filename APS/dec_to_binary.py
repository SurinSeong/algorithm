target = 74

# 변환 내장 함수 존재함.
print(bin(74))
print(hex(74))

# 변환 함수 만들어보기 - 문자열 (자료구조)
def dec_to_bin(target):
    binary_number = ""

    while target > 0:
        remain = target % 2    # 1) 2로 나눈 나머지를 변수에 저장한다.
        binary_number = str(remain) + binary_number    # 2) 2진수를 만들 변수에 더해준다.
        target //= 2    # 3) 몫으로 변경해준다.
    print(binary_number)

dec_to_bin(target)

# 변환 함수 만들어보기 - 리스트 (자료구조)
def dec_to_bin_v2(target):
    binary_number = []

    while target > 0:
        remain = target % 2
        binary_number.append(str(remain))
        target //= 2

    return ''.join(binary_number[::-1])

print(dec_to_bin_v2(target))


# 10진수에서 2진수 변환을 재귀 호출로
def dec_to_bin_recursion(target, bin_number):
    if target == 0:
        print(bin_number)
        return

    remain = str(target % 2)
    dec_to_bin_recursion(target//2, remain+bin_number)

dec_to_bin_recursion(target, '')


def dec_to_bin_recursion_v2(target):
    global binary_number

    if target == 0:
        return

    remain = str(target % 2)
    binary_number = remain + binary_number
    dec_to_bin_recursion_v2(target//2)

binary_number = ""
dec_to_bin_recursion_v2(target)
print(binary_number)

