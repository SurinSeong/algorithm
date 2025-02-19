import sys
from pathlib import Path

filename = Path.cwd() / 'solving-club/input/input_1225.txt'
sys.stdin = open(filename, 'r')

# 암호 만들기
# 덱 사용하기
# 덱으로 해도 느리다..

from collections import deque

T = 10

for _ in range(T):
    tc = int(input())
    arr = list(map(int, input().split()))
    
    arr = deque(arr)    # deque으로 업데이트
    
    diff = 1
    while True:
        # 1 감소 후 뒤로 이동
        tmp = arr.popleft() - diff    # diff 만큼 감소 후
        
        if tmp < 0:    # 음수라면
            tmp = 0
            
        arr.append(tmp)    # 뒤로 이동
        
        if tmp == 0:
            break    # 종료
        
        diff += 1
        
        if diff == 6:    # diff의 조건
            diff = 1
            
    print(f'#{tc} {" ".join(list(map(str, arr)))}')
    
# 덱이 더 빠른 이유 : 배열은 pop(0)를 하면 나머지를 새로운 배열로 복사하는 방법을 이용한다.
# 하지만, 덱은 연결 리스트 형식으로 배열을 복사하는 방법을 이용하지 않는다.  