a = 'F'
b = int(a, 16)
c = '1001'
d = int(c, 2)

print(b), print(d)

# int()와 같은 atoi() 함수 만들기
s = '123'
print(ord('0'))  # 48
print(ord('1'))  # 49


def atoi(string):
    i = 0
    for num in string:
        i = (ord(num) - ord('0')) + i*10
    return i


a = atoi(s)
print(a)