def solution(n, k):
    answer = []
    
    numbers = list(range(1, n+1))
    used = [0] * n
    
    def dfs(i, k):
        
        fact = 1
        
        for x in range(1, n-i):
            fact *= x
        
        if i == n:
            return True
        
        for x in range(n):
            if used[x]:    # 사용된 숫자이면
                continue
            
            if k < fact:
                answer.append(numbers[x])
                used[x] = 1
                if dfs(i+1, k):
                    return True
                used[x] = 0
                answer.pop()
            else:
                k -= fact
                
        return False
                
    dfs(0, k-1)
    
    return answer


print(solution(3, 5))