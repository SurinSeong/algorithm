# 줄 서는 방법 - 순열 문제
# n명의 사람이 일렬로 줄을 서고 있음.
# 1 ~ n번
# 사람의 수 : n
# 자연수 : k
# 사람을 나열하는 방법을 "사전" 순으로 함수 만들기
# 사전 순으로 k 번째를 출력

def solution(n, k):
    # 순열을 넣을 2차원 리스트
    answer = [[0] * n for _ in range(k)]
    
    for i in range(k):
        used = []
        numbers = [i+1 for i in range(n)]
        for j in range(n):
            if numbers[j] in used:
                j = (j+1) % n
            else:
            answer[i][j] = j+1
            used.append(j+1)
    
    return answer