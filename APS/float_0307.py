# 파이썬에서 실수 출력 방법
t1 = 10
t2 = 3.141592

print(f'변수 값은 {t1} 입니다.')
print(f'변수 값은 {t2} 입니다.')

# 소수점 출력 방법
# .소수점아래자리수f : 반올림해서 표현한다.
print(f'변수 값은 {t1} 입니다.')
print(f'변수 값은 {t2:.2f} 입니다.')

# [도전] 실수 값 출력해보기
# 0.1이 정확히 어떤 값으로 저장되었는지 출력
t = 0.1
print(f'{t:.20f}')

# 소수점을 포함한 2진 실수를 10진수로 변환하기
F = '1001.0011'

def bin_to_dec(bin_N):
    f_bin, b_bin = bin_N.split('.')

    # 정수 부분 먼저 처리하기
    f_dec = 0
    idx = 0
    for b in f_bin[::-1]:
        if b == '1':
            f_dec += 2**idx
        idx += 1

    # 실수 부분 처리
    b_dec = 0
    idx = -1
    for b in b_bin:
        if b == '1':
            b_dec += 2**idx
        idx -= 1

    return f_dec+b_dec

print(bin_to_dec(F))

# 10진수를 2진수로
def dec_to_bin(dec_N):
    f_dec, b_dec = int(dec_N), dec_N - int(dec_N)

    # 정수부분
    f_bin = ''
    while f_dec > 0:
        remain = f_dec % 2
        f_bin = str(remain) + f_bin
        f_dec //= 2

    # 소수 부분
    b_bin = ''
    while b_dec > 0:
        remain = int(b_dec * 2)
        b_bin += str(remain)
        b_dec = b_dec*2-remain

    return f_bin + '.' + b_bin

D = 12.375
print(dec_to_bin(D))