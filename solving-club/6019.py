# 기차 사이의 파리
# 거리 = 속력 * 시간

import sys
from pathlib import Path

filename = Path.cwd() / 'solving-club/input/input_6019.txt'
sys.stdin = open(filename, 'r')

# 함수
def go_to_the_train(a_loc, b_loc, f_loc, where):
    
    global A, B, F
    
    # 'B'로 가는 경우
    if where == 'B':
        # B와 F가 만나는 시간
        h = (f_loc - b_loc) / (B+F)
        # B와 F의 위치가 동일
        new_b_loc = new_f_loc = b_loc + B*h
        # A의 위치
        new_a_loc = a_loc - A*h
        # F가 이동한 거리
        fd = (f_loc - new_f_loc)
        
    # 'A'로 가는 경우
    else:
        # A와 F가 만나는 시간
        h = (a_loc - f_loc) / (A+F)
        # A와 F의 위치가 동일
        new_a_loc = new_f_loc = a_loc - A*h
        # B의 위치
        new_b_loc = b_loc + B*h
        # F가 이동한 위치
        fd = (new_f_loc - f_loc)
        
    return new_a_loc, new_b_loc, new_f_loc, fd


# 테스트 케이스 개수
T = int(input())

for t in range(1, T+1):
    D, A, B, F = map(int, input().split())
    # 파리가 가야 할 위치
    location = 'B'
    # 파리가 이동한 거리
    total_fd = 0
    # A, B기차, F의 위치
    A_loc, B_loc, F_loc = D, 0, D
    
    # 두 기차가 충돌할 때 까지 계속
    while (A_loc - B_loc) >= 1e-6:
        # B에서 시작     
        if location == 'B':
            A_loc, B_loc, F_loc, d = go_to_the_train(A_loc, B_loc, F_loc, location)
            total_fd += d
            location = 'A'
            
        # A에서 시작이라면
        if location == 'A':
            A_loc, B_loc, F_loc, d = go_to_the_train(A_loc, B_loc, F_loc, location)
            total_fd += d
            location = 'B'
            
    print(f'#{t} {total_fd}')