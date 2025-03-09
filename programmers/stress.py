"""
[피로도]
- 피로도 시스템(0 이상의 정수)이 있고
- 일정 피로도를 사용해서 던전 탐험
- 최소 피로도 : 탐험을 시작하기 위해 필요함.
- 소모 피로도 : 탐험을 마쳤을 때 소모됨.

- 하루에 한번씩 탐험할 수 있는 던전 존재
- 최대한 많이 탐험한다.
- 현재 피로도 : k
- dungeons : 2차원 배열 >> 행의 개수 1 <= <= 8
    - 최소 필요 피로도, 소모 피로도
"""
def solution(k, dungeons):
    answer = -1
    N = len(dungeons)
    visited = [False] * N   # 방문여부 확인 리스트

    def dfs(i, stress, total):    # stress : 현재의 피로도, total : 지금까지 다녀간 던전
        nonlocal answer, N
        
        answer = max(answer, total)
    
        if i == N:    # 모든 던전을 다 돌았다면
            return
        
        # 조건 만족하면
        if not visited[i]:
            if (dungeons[i][1] <= stress) and (dungeons[i][0] <= stress):     # 최소 필요 피로도 조건도 만족하고, 소모 피로도 보다도 남은 피로도가 크면
                visited[i] = True    # 방문 O
                dfs(0, stress-dungeons[i][1], total+1)
                visited[i] = False    # 백트래킹

        # 조건 만족하지 않으면
        dfs(i+1, stress, total)    # 다음으로 넘어가기
     
    dfs(0, k, 0)    
    
    return answer

k = 50
dungeons = [[50, 20], [10, 5], [30, 15], [20, 10]]

print(solution(k, dungeons))