"""
[가운데를 말해요]
- 백준이가 정수를 하나씩 외친다.
- 동생은 지금까지 백준이가 말한 수 중에서 '중간값'을 말해야 한다.
- 외친 수의 개수가 짝수 개라면 중간에 있는 두 수 중 작은 수 말하기

[조건]
- 1 <= N <= 100,000
- -10,000 <= 정수 <= 10,000
"""
# 중간값 찾는 함수
def find_mid_num(arr):
    N = len(arr)
    
    for i in range(N-1):    # 우선 주어진 정수들을 정렬시킨다.
        for j in range(i+1, N):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
                
    # 정렬된 리스트의 길이 // 2를 중간값으로 한다.
    if N % 2:    # 홀수라면
        return arr[N//2]
    return arr[N//2-1]



# 백준이가 외치는 정수의 개수
N = int(input())

# 백준이 외치는 정수 리스트
baekjoon = []

for i in range(N):
    # 백준이 외치는 정수
    b_num = int(input())
    baekjoon.append(b_num)    # 리스트에 정수 일단 추가
    
    # 동생이 말해야 하는 중간값 찾기
    mid_num = find_mid_num(baekjoon)
    print(mid_num)
  