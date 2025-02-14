# A0 B0 순서대로 해보기
A = 'XYPV'
B = 'EOGGXYPVSY'

result = ''

for b in range(len(B)):
    if b < len(A):
        result += (A[b] + B[b])
    else:
        result += B[b]

print(result)

# while문 사용

ai = bi = 0
len_a, len_b = len(A), len(B)

result = ''

while ai+bi < len_a+len_b:
    # A에서 가져올 문자가 남아있으면
    if ai < len_a:
        result += A[ai]
        ai += 1
    if bi < len_b:
        result += B[bi]
        bi += 1

print(result)

# 배열로 받고 join 을 이용해서 출력하는 경우
result = [0]*(len_a+len_b)

ai = bi = 0

while ai + bi < len_a + len_b:
    if ai < len_a:
        result[ai+bi] = A[ai]
        ai += 1
    if bi < len_b:
        result[ai+bi] = B[bi]
        bi += 1

print(''.join(result))


