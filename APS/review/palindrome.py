# 회문 검사
# 1. 주어진 문자열이 회문인지 판단
# 비교횟수만큼 반복 => len(str1) // 2
N = len(str1)
# 상태변수 플래그를 사용해 상황 판단에 도움이 될 수 있도록 한다.
flag = True

for i in range(N//2):
    if str1[i] != str1[N-1-i]:
        flag = False
        break
# 반복 종료 시 회문인지 아닌지 => 정상적으로 반복했는지, 아니면 break로 종료했는지
# 2. for~else : 파이써닉한 문법
N = len(str2)

for i in range(N//2):
    if str2[i] != str2[N-1-i]:
        pass
        
#---------------------------------------------------------------------
# 길이가 L인 회문 찾기
# 1. 시작 위치 고정
arr = 'BCBBCAAC'
N = len(arr)
L = 4 # 회문의 길이

# 회문의 횟수 구하는 함수
def check_palindrome(arr, N, L):
    """_summary_

    Args:
        arr (_list_): _description_
        N (_int_): _description_
        L (_int_): _description_

    Returns:
        _int_: _the_number_of_palindrome_
    """
    cnt = 0
    # 모든 행에 대해서 >> 행 우선 탐색
    for row in range(N):
        # 한 행에 대해서 
        for s in range(0, N-L+1): # 시작점
            e = s + L -1 # 끝점
            # 회문 판단
            for i in range(L//2):
                if arr[row][s+i] != arr[row][e-i]:
                    break
            else:
                cnt += 1
                
    # # 모든 행에 대해서 >> 열 우선 탐색
    for col in range(N):
        # 한 행에 대해서 
        for s in range(0, N-L+1): # 시작점
            e = s + L -1 # 끝점
            # 회문 판단
            for i in range(L//2):
                if arr[s+i][col] != arr[e-i][col]:
                    break
            else:
                cnt += 1
    return cnt

# 2차원 배열이라면?
ans = 0
# 모든 행에 대해 조사한다.
for row in arr:
    ans += check_palindrome(row, 8, L)
    
# 회문 두 번째
# 열을 확인하는 경우 zip을 사용하면 편하다.
# 문자열로 묶어서 사용하고 싶으면 join을 사용하면 된다.