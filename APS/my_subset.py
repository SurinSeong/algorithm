# 가지치기를 잘하면 불필요한 계산을 줄일 수 있다.

# # 완전 탐색
# def f(i, N):
#     if i == N:
#         print(bit)
#         # print(bit)
#         # 부분집합의 합은?
#         s = 0
#         for j in range(N):
#             if bit[j]:
#                 s += A[j]
#         print(s)
#     else:
#         bit[i] = 1   # bit[i] = 1
#         f(i+1, N)    # bit[i+1] 결정 하기 위해 이동
#         bit[i] = 0
#         f(i+1, N)

# A = [1, 2, 3]

# bit = [0]*len(A)

# f(0, len(A))



# # ======================================================= #
# def f(i, N, s): # i : 인덱스, N : 배열 크기, i-1까지 결정한 원소의 합
#     if i == N:
#         print(bit, s)
#     else:
#         bit[i] = 1    # bit[i]를 1로 결정
#         f(i+1, N, s+A[i])    # bit[i+1] 결정하러 이동
#         bit[i] = 0
#         f(i+1, N, s)

# A = [1, 2, 3]
# bit = [0]*len(A)
# f(0, len(A), 0)

# # ========================================================#
# 부분 집합의 합이 2인 경우를 찾는다면?
# def f(i, N, s,t): # i : 인덱스, N : 배열 크기, s : i-1까지 결정한 원소의 합, t : 찾는 합
#     if s > t:   # 찾는 합보다 커지면 중지
#         return

#     if i == N:
#         if s == t:
#             print(bit, s)
#     else:
#         bit[i] = 1    # bit[i]를 1로 결정
#         f(i+1, N, s+A[i], t)    # bit[i+1] 결정하러 이동
#         bit[i] = 0
#         f(i+1, N, s, t)

# f(0, len(A), 0, 2)

# # ----------------------------------------------------------------
# def f(i, N, s, t):  # i : 인덱스, N : 배열 크기, s : i-1까지 결정한 원소의 합, t : 찾는 합
#     if s == t:    # 찾는 값이면
#         print(bit, s)
#     if s > t:  # 찾는 합보다 커지면 중지
#         return
#     if i == N:
#         return
#     else:
#         bit[i] = 1  # bit[i]를 1로 결정
#         f(i + 1, N, s + A[i], t)  # bit[i+1] 결정하러 이동
#         bit[i] = 0
#         f(i + 1, N, s, t)


# f(0, len(A), 0, 2)

# # ------------------------------------------------------------------------
# # 왜 이리 추가할게 많아..
# """
# 전체의 합을 한번 구한다.
# 남은 원소의 합을 이용해서 백트래킹 가능하다.
# 남은 원소의 합을 다 더해도 찾는 값 미만인 경우 중단한다.
# """


# def f(i, N, s, t, rs):  # i : 인덱스, N : 배열 크기, s : i-1까지 결정한 원소의 합, t : 찾는 합, rs : 남은 원소의 합

#     global cnt
#     cnt += 1

#     if s == t:    # 찾는 값이면
#         print(bit, s)
#     elif s > t:  # 찾는 합보다 커지면 중지
#         return
#     elif i == N:    # 현재의 인덱스가 총 길이 만큼 되면
#         return
#     elif s + rs < t:    # 남은 원소를 다 더해도 찾을 수 없으면
#         return
#     else:
#         bit[i] = 1  # bit[i]를 1로 결정
#         f(i + 1, N, s + A[i], t, rs-A[i])  # bit[i+1] 결정하러 이동
#         bit[i] = 0    # 백트래킹
#         f(i + 1, N, s, t, rs-A[i])    # 백트래킹

# cnt = 0
# A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# bit = [0]*len(A)
# f(0, len(A), 0, 5, sum(A))


# ------------------------------------------------------------------------------- #
def f(i, N, s, t, rs):
    
    global cnt, result
    cnt += 1
    
    if s == t:
        print(bit, s)
        
        num_list = []
        for i in range(len(A)):
            if bit[i] == 1:
                num_list.append(A[i])
                
        result.append(num_list)
        
    elif s > t:
        return
    elif i == N:
        return
    elif s + rs < t:
        return
    else:
        bit[i] = 1
        f(i+1, N, s+A[i], t, rs-A[i])
        bit[i] = 0
        f(i+1, N, s, t, rs-A[i])
    
    return result
        

cnt = 0
A = [1, 2, 3, 4, 5]
bit = [0] * len(A)
result = []

result = f(0, len(A), 0, 3, sum(A))

# print(result)

