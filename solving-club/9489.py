import sys
from pathlib import Path

filename = Path.cwd() / 'solving-club/input/input_9489.txt'
sys.stdin = open(filename, 'r', encoding='utf-8')

# 고대 유적
# 해상도 NxM
# 가장 긴 구조물의 길이는?


# 사진 데이터의 개수
T = int(input())

for tc in range(1, T+1):
    # N,M
    N, M = map(int, input().split())
    picture = [list(map(int, input().split())) for _ in range(N)]
    
    max_building_length = 2
    
    for i in range(N):
        building_length_row = 0
        building_length_col = 0
        for j in range(M):
            
            # 행 확인
            if picture[i][j] == 1:
                building_length_row += 1
                max_building_length = max(max_building_length, building_length_row)
            else:
                max_building_length = max(max_building_length, building_length_row)
                building_length_row = 0
            

            # 열 확인
            if picture[j][i] == 1:
                building_length_col += 1
                max_building_length = max(max_building_length, building_length_col)
            else:
                max_building_length = max(max_building_length, building_length_col)
                building_length_col = 0
        
    
    print(f'#{tc} {max_building_length}')
                    
                
    