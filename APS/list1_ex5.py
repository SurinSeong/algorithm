# 찾는 값이 배열에 있으면 해당 원소의 인덱스, 없으면 -1을 idx에 넣기
'''
6 5
2 7 5 3 1 7
'''
# 원소의 개수와 찾는 값 받기
N, V = map(int, input().split())

# 배열 받기
arr = list(map(int, input().split()))

# 일단 없다고 가정
V_idx = -1

# 배열 돌기
for i in range(N):
    if arr[i] == V:
        V_idx = i
        # 찾았으니깐 끝내기
        break
    
print(V_idx)