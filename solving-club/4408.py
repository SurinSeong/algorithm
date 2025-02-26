# import sys
# from pathlib import Path
from collections import deque

# filename = Path.cwd() / 'solving-club/input/input_4408.txt'
# sys.stdin = open(filename, 'r')

"""
최단 시간에 모든 학생이 자신의 방으로 돌아간다.
방 : 400개
복도가 겹치면 같이 못들어감.
"""
def go_back(arr, n):
    # 앞에서부터 뺄 수 있도록 deque 설정
    arr_deque = deque(arr)
    
    # 인덱스 리스트
    idx_list = deque([i for i in range(n)])
    
    # 스택 설정
    stack = []
    
    # 첫 번째 요소 넣기
    first = arr_deque.popleft()
    idx_list.popleft()    # 인덱스도 빼주기
    stack.append(first)
    
    # 최소 이동 시간
    cnt = 0
    
    while arr_deque:    # 스택이 비지 않을 때까지
        
        current = arr_deque.popleft()    # 함께 옮길 수 있는지 여부를 확인할 대상
        current_idx = idx_list.popleft()    # 확인 대상의 인덱스스
        in_stack = stack.pop()
        
        # 마지막 인덱스가 진짜 마지막 인덱스라면
        if min(idx_list) == idx_list[0]:
            cnt += 1
        
        # 겹치면 따로 방 옮길 수 없음.
        if in_stack[-1] + 1 >= current[0]:
            stack.append(in_stack)    # 다시 넣기
            arr_deque.append(current)    # 확인한 대상은 뒤로 넣기
            idx_list.append(current_idx)    # 인덱스 다시 넣어주기
            
        # 겹치지 않으면 한 번에 방 옮기기 가능
        else:
            stack.append(current)    # 스택에 넣어주기
            idx_list.append(current_idx)    # 인덱스는 다시 넣어주기
    
    return cnt
                
                    
# 테스트 케이스 개수
T = int(input())

for tc in range(1, T+1):
    # 돌아가야 할 학생들의 수
    N = int(input())
    # 들어가야 할 학생 리스트
    student_list = []
    # 학생 수 만큼 반복
    for _ in range(N):
        here, move = map(int, input().split())
        student_list.append([min(here, move), max(here, move)])    # 어차피 겹치는 거는 똑같으니깐..
        
    # student_list 정렬시키기
    for i in range(N-1):
        for j in range(i, N):
            if student_list[i][0] > student_list[j][0]:
                student_list[i], student_list[j] = student_list[j], student_list[i]
                
    print(student_list)

    answer = go_back(student_list, N)

    print(f'#{tc} {answer}')