# Flatten
# 최고점과 최저점의 간격을 줄이기
# 가장 높은 곳에서 가장 낮은 곳으로 줄이기
# 옮긴 후 최고점-최저점

# 총 10개의 테스트 케이스
for t in range(1, 11):
    # 덤프횟수
    dump = int(input())
    # 각 상자의 높이 값
    heights = list(map(int, input().split()))

    # max, min 가정
    