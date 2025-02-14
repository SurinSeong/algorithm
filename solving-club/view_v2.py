# 조망권 확보 조건 : 왼쪽과 오른쪽으로 창문을 열었을 때, 양쪽 모두 거리 2이상의 공간 확보
# 조망권 확보 세대 수?

# 테스트 케이스 수
T = int(input())

# 각 테스트 케이스 별 문제 풀기
for t in range(1, T+1):
    
    # 건물의 개수
    N = int(input())
    # 건물 높이 리스트
    arr = list(map(int, input().split()))

    # 조망권 확보 총 세대 수
    total = 0

    for i in range(2, N-2):
        # 중심 건물 포함 5개의 요소 따로 빼기
        five_buildings = arr[i-2:i+3]
        # 중심 건물 변수 저장
        center = five_buildings.pop(2)
        # 주변 건물 중 가장 큰 건물 가정
        second_building = five_buildings[0]
        # 중심 건물의 주변 건물 조사
        for building in five_buildings[1:]:
            # 가정한 건물보다 더 높은 건물이 나온다면
            if second_building < building:
                # 중심 건물 제외 가장 큰 빌딩 확정
                second_building = building

        # 중심보다 더 높은 건물이 나오지 않았다면
        if center > second_building:
            total += (center - second_building)

    print(f'#{t} {total}')

