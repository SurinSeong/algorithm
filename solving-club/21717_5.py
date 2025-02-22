def solution(n, k):
    answer = []
    
    numbers = list(range(1, n+1))
    used = [0] * n
    
    def dfs(i, k):
        
        fact = 1
        
        for x in range(1, n-i):    # 팩토리얼 구하기
            fact *= x
        
        if i == n:    # 깊이가 n에 도달하면 순열 완성
            return
        
        for x in range(n):
            if used[x]:    # 사용된 숫자이면 건너뛰기
                continue
            
            # 현재 숫자를 선택하고 k번째 순열을 찾을 수 있는지 확인
            if k < fact:
                answer.append(numbers[x])    # 숫자를 순열에 추가한다.
                used[x] = 1    # 사용된 숫자라고 판단
                dfs(i+1, k)    # 깊이를 1 증가 시키며 순열 생성
                
            else:
                k -= fact    # k번째 순열을 건너뛰기 위해 k 조정
                
    dfs(0, k-1)
    
    return answer


print(solution(3, 5))