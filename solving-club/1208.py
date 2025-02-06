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

    # 정렬하기 - 가로는 항상 100, 건물 높이 1~100
    count = [0] * 100
    sorted_heights = [0] * 100

    # 카운팅
    for i in range(100):
        count[heights[i]-1] += 1

    # 누적합
    for i in range(1, 100):
        count[i] += count[i-1]

    # sorted_heights 에 정렬
    for i in range(100-1, -1, -1):
        count[heights[i]-1] -= 1
        sorted_heights[count[heights[i]-1]] = heights[i]

    # 정렬한 것 기준으로 뒤에서부터 앞으로 보내기

    min_idx, max_idx = 0, -1
    for i in range(dump):

        # 최소 인덱스 설정
        while sorted_heights[min_idx] >= sorted_heights[min_idx+1]:
            sorted_heights[min_idx], sorted_heights[min_idx+1] = sorted_heights[min_idx+1], sorted_heights[min_idx]
            min_idx += 1

        # 최대인 인덱스 설정
        while sorted_heights[max_idx] <= sorted_heights[max_idx-1]:
            sorted_heights[max_idx], sorted_heights[max_idx-1] = sorted_heights[max_idx-1], sorted_heights[max_idx]
            max_idx -= 1

        sorted_heights[min_idx] += 1
        sorted_heights[max_idx] -= 1

    print(f'#{t} {sorted_heights[-1]-sorted_heights[0]}')