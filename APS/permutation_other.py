# 이미 사용한 것들을 넣는 방식이 있다. used_list를 만드는..
def f(i, n, k, a):
    global cnt

    # result = []

    if i == n:    # p[i]를 모두 채운 경우
        cnt += 1
        print(f'{cnt} => {p}')    # 출력

        if cnt == k:
            a.append(p)

    else:
        for j in range(n):    # 아직 p에 사용하지 않은 숫자를 찾기
            if used[j] == 0:
                p[i] = arr[j]
                used[j] = 1    # arr[j]를 사용했다.
                f(i+1, n, k, a)
                used[j] = 0    # arr[j]를 다른 자리에서 사용할 수 있도록 상태 변경

    # return a


N = 3
arr = [1, 2, 3]    # 순열을 만들 숫자 모음
p = [0] * N    # 완성된 순열 넣는 리스트
used = [0] * N    # 이미 사용된 숫자 표시
cnt = 0
result = []

f(0, N, 5, result)

print(result)