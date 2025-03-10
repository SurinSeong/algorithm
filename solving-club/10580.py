"""
[전봇대]
- N개의 전선으로 연결
- 일대일 대응, 교차 가능
- 세 개 이상의 전선이 하나의 점에서 만나지 않는다.
- 총 교차점의 개수는?
"""
def find_parallel():
    # 1. 평행한 선의 개수 찾기

    pass

# 테스트 케이스 개수
T = int(input())

for tc in range(1, T+1):
    # 전선 개수
    N = int(input())
    # 두 전봇대에 있는 전선을 나타내는 배열
    cables = [[0]*N for _ in range(3)]
    parallel = 0
    for i in range(N):
        # 전선이 걸려 있는 고도
        A, B = map(int, input().split())
        cables[0][i], cables[1][i] = A, B
        cables[2][i] = A-B


    answer = 0
    print(f'#{tc} {answer}')