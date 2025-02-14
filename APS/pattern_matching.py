# 패턴 매칭

# t의 인덱스 i, p의 인덱스 j / t의 길이 = N, p의 길이 = M
# 조건 이용해서 반복하기
# target과 pattern의 요소가 다르면 target의 다음 칸 확인하기
# 같으면 target, pattern의 인덱스 모두 옆으로 옮겨서 맞는지 확인하기

# 패턴의 첫 번째 위치 구하기
def find_pattern(t, p):
    i = j = 0
    n = len(t)
    m = len(p)
    # 인덱스가 모두 범위 안에 있을 때
    while i < n and j < m:
        # target의 요소와 pattern의 요소가 다르면
        if t[i] != p[j]:
            # 인덱스 변경
            i = i - j + 1
            j = 0
        # 다르지 않다면
        else:
            i += 1
            j += 1
    # 만약 패턴을 찾았다면 (= 패턴의 인덱스 번호가 패턴의 길이와 동일해졌다면)
    if j == m:
        # 시작 위치 반환
        return i - j
    return -1


# 패턴의 개수 세기
def count_pattern(t, p):
    i = j = 0
    n = len(t)
    m = len(p)
    total = 0
    # target의 인덱스가 길이를 넘어가면
    while i < n:
        # 요소가 다르면 넘어가기
        if t[i] != p[j]:
            i = i - j + 1
            j = 0
        else:
            i += 1
            j += 1
        # 패턴 찾으면
        if j == m:
            # 개수 추가
            total += 1
            i = i - j + 1
            j = 0
    return total


target = 'TTTTTATTAATA'
pattern = 'TTA'

print(find_pattern(target, pattern))
print(count_pattern(target, pattern))
