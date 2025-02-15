# 화물 도크
# 24시간 운영 0~다음날0
# 최대한 많은 화물차 이용
# 앞 작업의 종료와 동시에 시작
import sys
from pathlib import Path

filename = Path.cwd() / 'solving-club/input/input_5202.txt'
sys.stdin = open(filename, 'r')


# 도크 세는 함수
def count_dock(i):
    # 1. 앞의 end와 뒤의 end 비교
    # 앞의 end가 뒤의 end와 같을 때
    if schedule[i][0] == schedule[i+1][0]:
        
        # 2. 앞의 시간과 뒤의 시간 비교
        # 앞의 시간이 뒤의 시간보다 짧으면
        if hours[i] < hours[i+1]:
            
            # 앞과 뒤의 자리 바꿔주기
            schedule[i], schedule[i+1] = schedule[i+1], schedule[i]
            hours[i], hours[i+1] = hours[i+1], hours[i]
            
            
    # 앞의 end가 뒤의 end와 다를 때 (앞의 end > 뒤의 end)
    else:
        # 앞의 시간이 뒤의 시간보다 짧으면
        if hours[i] < hours[i+1]:
            # 상태만 변경하고 끝낸다.
            return True
        
        # 앞의 시간이 뒤의 시간보다 같으면
        elif hours[i] == hours[i+1]:
            # 3. 앞의 start와 뒤의 end 비교
            # 앞의 start >= 뒤의 end
            if schedule[i][-1] >= schedule[i+1][0]:
                # 상태 변경
                return True
            else:
                # 순서 바꾸기
                schedule[i], schedule[i+1] = schedule[i+1], schedule[i]
                hours[i], hours[i+1] = hours[i+1], hours[i]
        
        # 앞의 시간이 뒤의 시간보다 길면
        else:
            # 앞의 start >= 뒤의 end
            if schedule[i][-1] >= schedule[i+1][0]:
                return True
            
    return False

# ------------------------------------------------------------------ #
# 테스트 케이스
T = int(input())

for tc in range(1, T+1):
    # 신청서 개수
    N = int(input())
    # 시간으로 변경해서 리스트에 저장하기
    hours = [0]*N
    schedule = [0]*N
    
    for i in range(N):
        start, end = map(int, input().split())
        hours[i] = end-start
        schedule[i] = [end, start]  # 끝나는 시간을 먼저 넣어줌.
    
    # 정렬 -> end를 기준으로 내림차순
    for i in range(0, N-1):
        for j in range(i+1, N):
            if schedule[i][0] < schedule[j][0]:
                # 자리 바꾸기
                schedule[i], schedule[j] = schedule[j], schedule[i]
                hours[i], hours[j] = hours[j], hours[i]
    
    # ----------------------------------------------------------------------- #
    cnt = 0
    
    for i in range(N-1):
        if count_dock(i):
            cnt += 1
    
    print(f'#{tc} {cnt}')
        
        
                
            

