# 유니코드
print(f'{ord("대"):x}')
print(chr(0xb300))

s1 = list(input())
print(s1)

s2 = input()
print(s2)

# s1, s2 둘다 인덱싱 가능
print(s1[1])
print(s2[1])

# 요소 변경해보기
s1[1] = 'e'
print(s1)

s2[1] = 'e'  # 일부만 바꾸는 것은 불가능
print(s2)

s2 = 'aec'  # 직접 변경은 가능
print(s2)

s3 = 'ab'*6
print(s3)

s_list = ['a', 'b', 'c']
print(''.join(s_list))