# 숫자로 이루어진 문자열 t, p
# t에서 p와 길이가 같은 부분 문자열 중 이 부분 문자열이 나타내는 수가 p가 나타내는 수보다 작거나 같은 것이 나오는 횟수는?

def solution(t, p):
    answer = 0

    # p의 길이
    p_len = len(p)

    for i in range(len(t)-p_len+1):
        same_len_with_p = t[i:i+p_len]
        print(same_len_with_p)

        if int(same_len_with_p) <= int(p):
            answer += 1

    return answer