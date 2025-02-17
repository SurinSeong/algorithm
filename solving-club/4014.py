# NxN 활주로 건설
# 숫자는 지형 높이
# 가로 or 세로로 건설
# 높이(1<=<=6)가 동일한 구간에서 건설 가능
# 경사로 : 길이-2<=x<=4, 높이 1 => 경사로 높이가 극복할 수 있도록
import sys
from pathlib import Path

filename = Path.cwd() / 'solving-club/input/input_4014.txt'
sys.stdin = open(filename, 'r', encoding='utf-8')


"""
[활주로 건설 조건]
0. 모든 높이가 동일해야 한다.
1. 하나의 라인에서 최대 높이보다 작은 것들이 경사로 길이보다 길어야 한다. (이때, 작은 것이 여러 개라면 각각 다 1씩 차이 나야 한다.)
2. 가장 높은 지형 주변에는 하나 낮은 것이 있어야 한다.

위의 조건과 반대가 되면 건설을 하지 못한다.

경사도의 길이 : 2 <= x <= 4
지형의 높이 : 1 <= <= 6
한 변의 길이 : 6 <= <= 20
"""
# 
def is_avaiable(line, n, w):
    # 가장 높은, 가장 낮은 높이
    max_num, min_num = max(line), min(line)
    
    cnt = 0
    
    for i in range(1, n):

        if line[i-1] == line[i]:
            cnt = 2
            
            if cnt == w:
                cnt = 1
            else:
                cnt += 1
                
            continue
        
        elif abs(line[i-1] - line[i]) != 1:
            return False
        
        else:
            if line[i-1] < line[i]:
                return False
            else:
                continue
        
            
    pass
    
                
def build_gradient(line, n, w):
    # 활주로 건설 가능하지 않다고 우선 판단
    result = False
    
    if len(set(line)) == 1:    # 모든 지형의 높이가 동일하다면
        result = True
        return result
    
    elif is_avaiable(line, n, w):
        result = True
        return result
    
    return result
        
        
# 테스트 케이스 개수
T = int(input())

for test_case in range(1, T+1):
    # 지도의 한 변의 크기, 경사로의 길이
    N, X = map(int, input().split())
    
    # 지형 정보
    fields = [[int(num) for num in input().split()] for _ in range(N)]

    cnt = 0
    
    # 행 확인
    for field_row in fields:
        if build_gradient(field_row, N, X):
            cnt += 1

    # 열 확인
    for field_col in zip(*fields):
        if build_gradient(field_col, N, X):
            cnt += 1
    
    print(f'#{test_case} {cnt}')