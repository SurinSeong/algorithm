import sys
from pathlib import Path

filename = Path.cwd() / 'solving-club/input/input_10761.txt'
sys.stdin = open(filename, 'r', encoding='utf-8')

# 신뢰
# 로봇 : 오렌지 & 블루
# **서로 다른** 복도 실험
# 1 ~ 100 정수로 구분되는 100개의 버튼
# 버튼 K : 시작점에서 K미터 떨어져 있음.
# 두 로봇은 **버튼 1**에서 시작
# 매 1초마다 -> 로봇은 복도의 양 방향 중 하나로 1미터 걷거나, 자신의 위치에 있는 버튼을 누르거나, 아무것도 안함.
# 테스트 : 여러 개의 버튼 수열로 표시. 수열에 표시된대로 눌러야 함.
# O x : 오렌지 눌러!, B x : 블루 눌러!
# 동시에 못누른다.
# 테스트를 끝낼 수 있는 가장 빠른 시간은?


def search_other_robot(first_robot):
    pass


def move_robots(round_list):
    # 총 걸린 시간
    total_second = 0
    # O, B 로봇의 시작 위치
    oi, bi = 1, 1
    
    # 처음 옮겨야 할 것
    first_robot = round_list[0][0]
    first_location = round_list[0][1]
    
    next_robot = ''
    
    # O, B가 눌러야할 위치 각각 파악하기
    for i, round in enumerate(round_list[1:]):
        color = round[0]
        button_idx = round[1]
        
        if color != first_robot:
            next_robot = color
            next_location = button_idx
            
        
        
        
        
    
    
            
                
        total_second += 1        
                
    return total_second        
    
        
TC = int(input())

for tc in range(1, TC+1):
    # 버튼 배열
    button_list = input().split()
    # 눌러야 하는 버튼의 개수
    N = int(button_list.pop(0))
    # 버튼 리스트 생성
    button_O, button_B = [0]*101, [0]*101
    # 라운드
    rounds = [[0] for _ in range(N)]
    
    for i in range(len(button_list)//2):
        
        robot = button_list[i*2]
        button = int(button_list[i*2+1])
        
        round[i] = [robot, button]
        
        if robot == 'O':
            button_O[button] = 1
            
        else:
            button_B[button] = 1
    
    print(round)
    
    # 이동
    
        
    
    # total_seconds = move_robots(sum(button_O), sum(button_B))
        
    
    print(f'#{tc} ')  # {total_seconds}