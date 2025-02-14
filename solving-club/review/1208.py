# flatten
# 최고점, 최저점 찾기
# 가로 100
import sys
from pathlib import Path

filename = Path.cwd() / 'solving-club/input/input_1208.txt'
sys.stdin = open(filename, 'r')

for tc in range(1, 11):
    # 덤프횟수
    dump = int(input())
    # 상자들
    boxes = list(map(int, input().split()))
    
    # 덤프 횟수가 남아있거나, '가장 높은-낮은'이 1보다 큰 경우
    while dump > 0:
        # 가장 높은, 낮은 먼저 가정 (조건)
        highest, lowest = max(boxes), min(boxes)
        # 빠른 종료
        if highest - lowest <= 1:
            break
        # highest, lowest idx 찾기
        for i in range(100):
            if boxes[i] == highest:
                max_idx = i
                break
        for i in range(100):    
            if boxes[i] == lowest:
                min_idx = i
                break
            
        # 상자 옮겨주기
        boxes[max_idx] -= 1
        boxes[min_idx] += 1
        
        # 덤프횟수 줄여주기
        dump -= 1
        
    print(f'#{tc} {max(boxes) - min(boxes)}')