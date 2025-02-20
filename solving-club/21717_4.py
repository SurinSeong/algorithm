def solution(n, k):
    # # 순열을 넣을 2차원 리스트
    # answer = [[0] * n for _ in range(k)]
    # rotation = factorial(n) // n
    cnt = 0
    numbers = [i+1 for i in range(n)]

    for i in range(1, 1 << n):    # 부분 집합의 개수
        elements = []
        for j in range(n):    # 원소의 수만큼 비트 비교
            if i & (1 << j):    # i의 j번 비트가 1인 경우
                elements.append(numbers[j])    # 숫자 추가
        cnt += 1
        if cnt == k:
            break

    return elements

print(solution(3, 5))