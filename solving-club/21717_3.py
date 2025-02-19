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
        
        used = []    # 이미 순열에 사용한 숫자 리스트
        
        numbers = [i+1 for i in range(n)]    # 순열에 사용할 숫자 리스트
        
        # answer[i][0] = (i // (n-1)) + 1
        # used.append(answer[i][0])
        
        for j in range(n-1, -1, -1):    # 뒤에서 부터 넣기기
            
            idx = 0    # 순열에 사용할 숫자 가리키는 인덱스
        
            while True:
                if numbers[idx] in used:    # 만약 이미 사용한 숫자라면
                    idx = (idx+1) % n    # 인덱스 업데이트
                    continue
                
                elif answer[i-1][j] == numbers[idx]:
                    idx = (idx+1) % n
                    continue
                
                answer[i][j] = max()
                used.append(numbers[idx])
                break
    
    return answer

print(solution(3, 5))