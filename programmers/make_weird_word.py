def solution(s):
    answer = ''

    # 공백을 대체하기!
    s = ''.join(['-' if char == ' ' else char for char in s])

    start = -1

    for char in s:

        if char.isalpha():
            start += 1
            # 짝수번째 문자
            if start % 2 == 0:
                answer += char.upper()
            else:
                answer += char.lower()
        else:
            start = -1
            answer += ' '

    return answer