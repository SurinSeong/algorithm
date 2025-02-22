# 팩토리얼 함수
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
    

# k번째 순열 구하기
def solution(n, k):
    answer = []

    # 숫자 리스트 생성
    numbers = list(range(1, n+1))
    
    # 사용 여부 확인 리스트
    used = [0] * n
    
    k -= 1    # 0부터 시작하기 때문에
    
    # n! ~ 1!까지 차례대로 계산
    for i in range(n, 0, -1):
        fact = factorial(i-1)
        
        # k가 어떤 범위에 속하는지 확인한다.
        idx = k // fact
        cnt = -1
        
        for j in range(n):
            if not used[j]:    # 0이면 카운트 올리기
                cnt += 1
                
            if cnt == idx:    # 범위 값이랑 카운트 값이 같다면
                answer.append(numbers[j])
                used[j] = 1
                break
            
        k %= fact
    
    return answer

# print(solution(3, 5))
# print(factorial(3))