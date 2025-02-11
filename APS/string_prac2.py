# 제시된 길이를 가진 회문의 개수
# 인덱스 사용해서 풀어보기
"""
4
CBBCBAAB
CCCBABCB
CAAAACAB
BACCCCAC
AABCBBAC
ACAACABC
BCCBAABC
ABBBCCAA
"""
# 1. 일단 한 줄에서만 찾아보기
# 제시된 길이
N = int(input())

# alpha = input()

# 회문 개수
total = 0

# # 회문 확인 구간
# for i in range(len(alpha)-N+1):
#     check_word = alpha[i:i+N]
#     # 회문의 길이 절반 만큼 비교
#     for n in range(N//2):
#         # 양 끝부터 비교
#         if check_word[n] != check_word[N-n-1]:
#             # 같지 않으면 다음
#             break
#     # 비교 했는데 같으면
#     else:
#         # 개수 추가
#         total += 1
#         # 회문인 단어 출력해보기
#         print(check_word)


# 2. 가로 세로 전부 찾아보기
def find_palindrome(arr, n):
    # 회문 개수
    palindrome = 0

    for i in range(8):
        for j in range(8-n+1):
            check_word = arr[i][j:j+n]
            # 회문의 절반 길이 만큼 비교
            for k in range(n//2):
                # 양 끝부터 비교
                if check_word[k] != check_word[n-k-1]:
                    break
            else:
                palindrome += 1

    return palindrome


matrix = [list(input()) for _ in range(8)]
# 전치
matrix_T = list(map(list, zip(*matrix)))

result1 = find_palindrome(matrix, N)
result2 = find_palindrome(matrix_T, N)

print(result1 + result2)




