import sys
from pathlib import Path

filename = Path.cwd() / 'solving-club/input/input_1926.txt'
sys.stdin = open(filename, 'r')

# 간단한 369 게임
# 3, 6, 9가 들어가 있는 수는 말하지 않음 -> 박수
# 박수는 해당 숫자가 들어간 개수 만큼 치기

def find_369(n):
    cnt = 0
    while (n // 10) != 0:
        
        if (n % 10) in [3, 6, 9]:
            cnt += 1
        
        n //= 10
    
    if n in [3, 6, 9]:
        cnt += 1
        
    return cnt


# 1 ~ N
N = int(input())

for num in range(1, N+1):
    if find_369(num) == 0:
        print(num, end=' ')
    else:
        print('-'*find_369(num), end=' ')