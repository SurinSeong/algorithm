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
def find_mid_num():
    for i in range(len(baekjoon)):
        ci, pi = i, i - 1    # 이전의 인덱스
        while pi > 0:    # 0보다 크면 비교 시작
            if baekjoon[pi] > baekjoon[ci]:    # 이전보다 작으면
                baekjoon[pi], baekjoon[ci] = baekjoon[ci], baekjoon[pi]    # 바꿔주기
                ci -= 1
                pi -= 1    # 인덱스 업데이트
                
            else:    # 작지 않으면 바꾸지 않는다.
                break
            
        print(baekjoon[i//2])


# 백준이가 외치는 정수의 개수
N = int(input())

# 백준이 외치는 정수 리스트
baekjoon = []

for i in range(N):

    b_num = int(input())    # 현재 외치는 정수
    baekjoon.append(b_num)
    
# 동생이 말해야 하는 중간값 찾기
find_mid_num()
  