# import sys
# from pathlib import Path
#
# filename = Path.cwd() / 'solving-club/input/input_5202.txt'
# sys.stdin = open(filename, 'r')

def dfs(start, subset):
    global answer

    if start == N:
        answer = max(answer, len(subset))
        return

    for i in range(start, N):
        if subset:
            ce, cs = applies[i][0], applies[i][1]
            pe, ps = subset[-1][0], subset[-1][1]

            if ps < ce:    # 시간이 겹치면
                continue    # 통과

        dfs(i+1, subset+[applies[i]])



# 테스트 케이스
T = int(input())

for tc in range(1, T+1):

    # 신청서
    N = int(input())

    # 신청서 리스트 만들기
    applies = []
    for _ in range(N):
        s, e = map(int, input().split())
        gap = e - s
        applies.append([e, s, gap])

    # 끝 시간을 기준으로 정렬
    applies = sorted(applies, key=lambda x: (-x[0], x[2]))

    # pre_end = applies[0][0]
    # pre_start = applies[0][1]

    answer = 1

    dfs(0, [])

    print(f'#{tc} {answer}')



