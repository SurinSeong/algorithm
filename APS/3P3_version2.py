# 순열 (완전 탐색)
"""
5
1 5 8
4 8 2
4 5 5
9 0 1
8 8 8
"""

# 테스트 케이스 개수 받기
T = int(input())

for t in range(1, T+1):
    print(f'#{t}')
    # 내가 원하는 숫자 3개 입력하기
    arr = list(map(int, input().split()))

    # 3중 for문으로 모든 경우의 수 출력해보기
    for num1 in arr:
        for num2 in arr:
            if num1 != num2:
                for num3 in arr:
                    if (num3 != num1) and (num3 != num2):
                        print(num1, num2, num3)
    else:
        print(arr)
