# 패턴 매칭
target = 'TTTTTATTAATA'
pattern = 'TTA'

# t의 인덱스 i, p의 인덱스 j / t의 길이 = N, p의 길이 = M
# 이중 for문
# target에서 pattern을 비교할 시작 위치 인덱스
# pattern에서 비교할 위치 인덱스
# break에 걸리지 않고 for가 끝난 경우 실행 (for-else에서 else 부분)
# 패턴이 없으면 -1

# 패턴의 위치 구하기
def search_pattern(t, p):
    n = len(t)
    m = len(p)
    # 패턴과의 위치를 비교할 인덱스 범위 설정
    for i in range(n - m + 1):
        for j in range(m):
            if t[i+j] != p[j]:
                break
        else:
            return i
    return -1


# 패턴의 개수 세기
def count_pattern(t, p):
    n = len(t)
    m = len(p)
    total = 0
    for i in range(n - m + 1):
        for j in range(m):
            if t[i+j] != p[j]:
                break
        else:
            total += 1
    return total


print(search_pattern(target, pattern))
print(count_pattern(target, pattern))
