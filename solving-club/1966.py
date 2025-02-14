# N 길이의 숫자열을 오름차순으로 정렬하여 출력하기
# 5 <= N <= 50
import sys
from pathlib import Path

filename = Path.cwd() / 'solving-club/input/input_1966.txt'
sys.stdin = open(filename, 'r')

# 테스트 케이스 수 받기
T = int(input())

for t in range(1, T+1):
    # 숫자열의 길이
    N = int(input())
    # 숫자열 받기
    number_list = list(map(int, input().split()))
    
    changed = True
    
    while changed:
        for i in range(1, N):
            # 만약 앞의 수가 뒤의 수보다 크면
            if number_list[i-1] > number_list[i]:
                # 자리 바꿔주기
                number_list[i-1], number_list[i] = number_list[i], number_list[i-1]
                break
        # for 문 다 돌 때까지 끝내기 못했다면
        else:
            # changed의 상태를 바꿔주기
            changed = False
    
    print(f'#{t} {" ".join([str(num) for num in number_list])}')