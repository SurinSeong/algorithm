# # 자연수 n이 매개변수로 주어질 때, 연속된 자연수들로 n을 표현하는 방법의 수
# # 완전 탐색
## 다시 다시 다시 다시 다시

n = 15
answer = 0


for i in range(1, n+1):
    total = 0
    for j in range(i, n+1):
        total += j
        if total == n:
            answer += 1
            break
        elif total > n:
            break

print(answer)

