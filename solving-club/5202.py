# 화물 도크
# 24시간 운영 0~다음날0
# 최대한 많은 화물차 이용
# 앞 작업의 종료와 동시에 시작
import sys
from pathlib import Path

filename = Path.cwd() / 'solving-club/input/input_5202.txt'
sys.stdin = open(filename, 'r')
        

# 테스트 케이스
T = int(input())

for tc in range(1, T+1):
    # 신청서 개수
    N = int(input())
    # 시간으로 변경해서 리스트에 저장하기
    hours = [0]*N
    applies = [0]*N
    
    for i in range(N):
        start, end = map(int, input().split())
        hours[i] = end-start
        applies[i] = [start, end]
    
    # 정렬
    for i in range(0, N-1):
        for j in range(i+1, N):
            if applies[i][-1] > applies[j][-1]:
                applies[i], applies[j], applies[j], applies[i]
                hours[i], hours[j] = hours[j], hours[i]
    
    print(applies)
    print(hours)
                
    
    # # 24시간이 가득 찰 때까지 더해주기
    # total = 24
    # cnt = 0
    # while True:
    #     if total > 24:
    #         break
    #     if cnt == N:
    #         break
        
    #     total -= hours[cnt]
    #     cnt += 1
        
    # print(cnt)
    
    
    
    # print(f'#{tc} {max_cnt}')
        
        
                
            

