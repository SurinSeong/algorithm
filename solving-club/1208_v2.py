# Flatten
# 최고점과 최저점의 간격을 줄이기
# 가장 높은 곳에서 가장 낮은 곳으로 줄이기
# 옮긴 후 최고점-최저점

import sys
from pathlib import Path

filename = Path.cwd() / 'solving-club/input/input_1208.txt'
sys.stdin = open(filename, 'r')

# 함수로 만들기
def flatten(dump, box_list):
    # max, min 가정
    min_box, max_box = 101, 0
    
    # 덤프 횟수 만큼 반복
    while (dump >= 0) and (abs(max_box - min_box) > 1):
        # min, max 찾기
        for n in range(100):
            if (min_box >= box_list[n]):
                min_box = box_list[n]
                min_idx = n
            if (max_box <= box_list[n]):
                max_box = box_list[n]
                max_idx = n
        
        dump -= 1
        
        min_box = box_list[min_idx]
        max_box = box_list[max_idx]
                
        # 최소인 상자에는 +1       
        box_list[min_idx] += 1
        # 최대인 상자에는 -1
        box_list[max_idx] -= 1
        
    return max_box-min_box

# 총 10개의 테스트 케이스
for t in range(1, 11):
    # 덤프횟수
    dump = int(input())
    # 각 상자의 높이 값
    box_list = list(map(int, input().split()))

    result = flatten(dump, box_list)            
    
    print(f'#{t} {result}')
    
    
        