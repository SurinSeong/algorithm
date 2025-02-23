import sys
from pathlib import Path

filename = Path.cwd() / 'solving-club/input/input_4880.txt'
sys.stdin = open(filename, 'r')

# 가위바위보가 그려진 카드를 이용해 토너먼트로 한 명을 뽑기
"""
- 1 ~ N번까지 N명의 학생이 N장의 카드를 나눠갖는다.
- 전체를 두 그룹으로 나누고, 그룹의 승자끼리 카드를 비교해 이긴사람이 최종 승자
- 그룹 승자를 다시 두 그룹으로 나누기
    - i ~ (i+j)//2
    - (i + j)//2 + 1 ~ j
- 1 : 가위, 2 : 바위, 3 : 보
- 같은 카드라면 번호가 작은 쪽을 승자로
- 처음 선택한 카드는 바꾸지 않음.
- 분할 정복 문제 같아..
"""
def game(arr, n):
    i = 0
    j = n-1
    
    if j >= 2:
        group1, group2 = arr[i:(i+j)//2+1], arr[(i+j)//2+1:j+1]
        game(group1, len(group1))
        game(group2, len(group2))
        
    else:
        if ((arr[i] == 1) and (arr[j] == 2)) or ((arr[i] == 2) and (arr[j] == 3)) or ((arr[i] == 3) and (arr[j] == 1)):
            return j
        
        else:
            return i



T = int(input())

for tc in range(1, T+1):
    # 인원수
    N = int(input())
    # 카드
    cards = list(map(int, input().split()))
    
    result = 0
    
    print(f'#{tc} {result}')