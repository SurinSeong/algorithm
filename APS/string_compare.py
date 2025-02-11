# 문자열 비교 함수
# 아스키 코드 순으로 비교
s1 = 'ab'
s2 = 'ac'
s3 = 'AC'
s4 = 'abc'
s5 = '1ab'
s6 = ' ab'

print(s1 < s2)  # True
print(s2 < s3)  # False
print(s1 < s6)  # False
print(s4 < s5)  # False
