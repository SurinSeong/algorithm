import sys
from pathlib import Path

filename = Path.cwd() / 'solving-club/input/input_3499.txt'
sys.stdin = open(filename, 'r')

# 퍼펙트 셔플
# 카드 덱을 정확히 절반으로 나누고
# 나눈 것들에서 교대로 카드를 뽑아
# 새로운 덱을 만드는 것
# N이 홀수이면 먼저 놓는 쪽에 한장이 더 들어간다.

# 테스트 케이스 개수
T = int(input())

for tc in range(1, T+1):
    # 카드 개수
    N = int(input())
    
    # 카드 이름 받기 (공백 구분, 80이하)
    cards = input().split()
    
    # 새로 정렬할 리스트
    perfect_shuffle = [0]*N
    
    part1 = cards[:(N-1)//2+1]
    part2 = cards[(N-1)//2+1:]
    for i in range(N//2):
        perfect_shuffle[i*2] = part1[i]
        perfect_shuffle[i*2+1] = part2[i]
    
    if N % 2:
        perfect_shuffle[-1] = part1[-1]
        
    print(f'#{tc} {" ".join(perfect_shuffle)}')
    
    