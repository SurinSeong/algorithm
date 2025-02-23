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
def divide_and_conquer(arr, n):
    # 카드의 개수가 하나 이하이면 리스트 그래도 반환
    if n <= 1:
        return arr
    
    # 요소의 개수가 2개 이상인 경우
    # 두 그룹으로 나누기 위해 중산 숫자를 저장한다.
    i, j = 0, n-1
    middle = (i+j)//2+1
    group1 = divide_and_conquer(arr[:middle], len(arr[:middle]))
    group2 = divide_and_conquer(arr[middle:], len(arr[middle:]))
    
    # 새로 정렬한 리스트
    result = []
    
    # 두 그룹을 분할 정복하기
    # 두 그룹의 요소가 다 있는 경우
    while group1 and group2:
        if ((group1[0] == 1) and (group2[0] == 2)) or ((group1[0] == 2) and (group2[0] == 3)) or ((group1[0] == 3) and (group2[0] == 1)):
            result.append(group2.pop())
        else:
            result.append(group1.pop())
    
    while group1:
        result.append(group1.pop())
        
    while group2:
        result.append(group2.pop())
    
    return result



T = int(input())

for tc in range(1, T+1):
    # 인원수
    N = int(input())
    # 카드
    cards = list(map(int, input().split()))
    
    result = 0
    
    print(f'#{tc} {result}')