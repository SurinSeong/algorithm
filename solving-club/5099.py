import sys
from pathlib import Path

filename = Path.cwd() / 'solving-club/input/input_5099.txt'
sys.stdin = open(filename, 'r')

"""
피자 굽기
- N개의 피자를 동시에 구울 수 있음.
- 치즈가 모두 녹으면 화덕에서 꺼낸다. (치즈의 양은 피자마다 다름)
- 1~M까지 M개의 피자를 순서대로 화덕에 넣음. 치즈의 양에 따라 녹는 시간이 다르기 때문에 꺼내는 순서는 바뀔 수 있음.
- 가장 마지막 까지 남아있는 피자 번호는?

[규칙]
- 1번 위치에서 넣거나 뺄 수 있음.
- 화덕 내부의 피자 받침은 1번에서 잠시 꺼내 상태 확인 가능
- 치즈의 양 C -> 한 바퀴 돌고 꺼내면 C//2
- C가 0이되면 꺼내고 남은 피자 넣음
"""
T = int(input())

for test_case in range(1, T+1):
    # 화덕의 크기, 피자 개수
    N, M = map(int, input().split())
    # 치즈양
    C = list(map(int, input().split()))
    
    q = [0]*N
    pointer = 0
    
    # 초기 상태 설정하고 들어가기
    for i in range(N):
        q[i] = [i, C[i]]
    
    next_idx = N
    
    while True:
        
        if q[pointer] is not None:    # 아직 채울 수 있는 것이 남아있을 때
            if q[pointer][-1] == 0:    # 만약 치즈가 다 녹았다면
                if next_idx < M:    # 추가할 수 있는 인덱스 번호가 남아있다면
                    q[pointer] = [next_idx, C[next_idx]]    # 추가해주기
                    next_idx += 1    # 인덱스 번호 업데이트
                else:    # 추가할 수 있는 인덱스 번호가 없다면
                    q[pointer] = None    # 빈자리로 만들기
                
            elif q[pointer][-1] != 0:    # 아직 치즈가 다 녹지 않았다면
                q[pointer][-1] //= 2    # 치즈 녹이기
                if q[pointer][-1] == 0:  # 만약 치즈가 다 녹았다면
                    if next_idx < M:
                        q[pointer] = [next_idx, C[next_idx]]    # 
                        next_idx += 1
                    else:
                        q[pointer] = None
        
        pointer = (pointer + 1) % N    # 포인터 위치 변경
        
        # 빈자리가 아닌 개수
        not_none = []
        
        for i in q:
            if i is not None:    # 만약 빈자리가 아니라면
                not_none.append(i[0])    # 리스트에 인덱스 넣어주기
        
        if len(not_none) == 1:    # 만약 빈자리가 아닌 개수가 하나이면
            break    # 끝내기
    
    print(f'#{test_case} {not_none[0]+1}')