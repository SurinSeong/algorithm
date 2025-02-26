import sys
from pathlib import Path

filename = Path.cwd() / 'solving-club/input/input_4008.txt'
sys.stdin = open(filename, 'r')

"""
[숫자 만들기]
N개의 숫자가 적혀있는 게임판
연산자의 우선 순위는 고려하지 않고 왼쪽에서 오른쪽으로 차례대로 계산
연산자 카드 개수의 총 합은 항상 N-1이다.
N은 3이상 12이하의 정수
숫자 순서는 지정
나눗셈은 소수점 이하 버리기
"""

# 풀이 시간 : 8시 20분 ~ 46분 / 10:12~

def symbol_perm(i, n):
    
    global symbol_perms
    
    p = symbol_list
    
    if i == n-1:
        perm = p
        make_expression(perm)
    
    else:
        for j in range(i, n-1):
            p[i], p[j] = p[j], p[i]
            symbol_perm(i+1, n)
            p[i], p[j] = p[j], p[i]


# 완성된 수식 만들기
def make_expression(perm):
    # 합을 넣을 리스트
    global sum_list
    
    result = number_list[0]
    
    for i, symbol in enumerate(perm, 1):
        if symbol == '+':
            result += number_list[i]
        elif symbol == '-':
            result -= number_list[i]
        elif symbol == '*':
            result *= number_list[i]
        elif symbol == '/':
            result /= number_list[i]
    
    sum_list.append(int(result))
    
    # return total_list


# 테스트 케이스 개수
T = int(input())

for tc in range(1, T+1):
    # 숫자의 개수
    N = int(input())
    
    # 연산자 카드 + - * /
    symbol_counts = list(map(int, input().split()))
    
    symbol_list = []
    
    for i, num in enumerate(symbol_counts):
        if i == 0:
            for _ in range(num):
                symbol_list.append('+')
        elif i == 1:
            for _ in range(num):
                symbol_list.append('-')
        elif i == 2:
            for _ in range(num):
                symbol_list.append('*')
        else:
            for _ in range(num):
                symbol_list.append('/')
            
    # 숫자 카드
    number_list = list(map(int, input().split()))
    
    # 기호 순서 조합
    symbol_perms = []
    
    # 합 리스트
    sum_list = []
    
    symbol_perm(0, N)
    
    answer = max(sum_list) - min(sum_list)
    
    print(f'#{tc} {answer}')