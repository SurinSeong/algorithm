# flatten

# 최고점, 최저점 찾기
# 가로 100

for tc in range(1, 11):
    # 덤프횟수
    dump = int(input())
    # 상자들
    boxes = list(map(int, input().split()))

    while True:
        highest, lowest = max(boxes), min(boxes)
        # box 의 min-max 차가 1이하인 경우 끝
        if highest - lowest <= 1:
            break
