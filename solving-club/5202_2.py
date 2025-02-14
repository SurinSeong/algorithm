import sys
from pathlib import Path

filename = Path.cwd() / 'solving-club/input/input_5202.txt'
sys.stdin = open(filename, 'r')

# 테스트 케이스
T = int(input())

for tc in range(1, T+1):
    # 신청서
    N = int(input())
    # 신청서 리스트 만들기
    applies = [list(map(int, input().split())) for _ in range(N)]
    new_applies = sorted(applies, key=lambda x:x[-1], reverse=True)
    print(new_applies)
    
    # 빈 신청서
    schedule = [0]*25
    
    schedule[new_applies[0][0]] += 1
    schedule[new_applies[0][-1]] += 1
    
    for i in range(1, N):
        if schedule[new_applies[i][0]] == 0:
            schedule[new_applies[i][0]] += 1
        if schedule[new_applies[i][-1]] == 0:
            schedule[new_applies[i][-1]] += 1

            
    print(schedule)