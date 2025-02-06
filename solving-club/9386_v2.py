# 연속한 1의 개수
# N개의 0과 1로 이루어진 수열
# 연속한 1의 개수 중 최댓값

# 테스트 케이스 수
T = int(input())

# T번 반복
for t in range(1, T+1):
    # 수열의 길이
    N = int(input())
    # 수열
    zero_one = input().split('0')
    
    