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
        # 해당 인덱스가 중심 건물임.
        center = arr[i]
        # 중심 건물의 주변 건물(-2, +2) 조사
        for j in range(i-2, i+3):
            # 중심보다 더 높은 건물이 나온다면
            if center < arr[j]:
                # 중심 건물 자격 박탈
                center = arr[j]
                # 끝내기
                break

        # 중심보다 더 높은 건물이 나오지 않았다면
        if center == arr[i]:
            # 중심 건물을 제외하고 가장 높은 건물 구하기
            second_max = arr[i-2]   # 가정
            # 다시 중심 주변 건물 확인
            for j in range(i-1, i+3):   # 가정한 인덱스 제외하고
                # 중심 건물 아니면 중심 건물 다음으로 큰 건물 구하기
                if i != j:
                    # second_max 구하기
                    if second_max < arr[j]:
                        second_max = arr[j]
            # 총 세대 수에 넣어주기
            total += (arr[i] - second_max)

    print(f'#{t} {total}')

