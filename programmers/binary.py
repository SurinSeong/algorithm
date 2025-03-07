# # 0과 1로 이루어진 어떤 문자열 x에 대한 이진 변환
# '''
# 1. x의 모든 0을 제거합니다.
# 2. x의 길이를 c라고 하면, x를 "c를 2진법으로 표현한 문자열"로 바꿉니다.
# '''
# # s가 "1"이 될 때까지 계속해서 s에 이진 변환을 가했을 때
# # 이진 변환의 횟수와 변환 과정에서 제거된 모든 0의 개수

# 이진 변환 함수
def change_to_binary(number):
    binary = ''
    while number != 1:
        binary += str(number % 2)
        number //= 2
        
    binary += str(number)
    
    return binary[::-1]


def solution(s):
    # 이진 변환 횟수
    changed_number = 0
    # 제거된 0의 개수
    delete_zero = 0

    # s를 '1'까지 만들기
    while True:

        print(f'=== {changed_number + 1}번 ===')

        # s가 '1'이면 끝내기
        if s == '1':
            break

        # s가 '1'이 아니면
        else:
            # 0 지운 문자열
            no_zero = ''.join([one for one in s if one == '1'])
            print(no_zero)

            delete_zero += (len(s) - len(no_zero))
            print(delete_zero)

            # 길이로 이진 변환하기
            c = len(no_zero)

            s = change_to_binary(c)

            # 숫자 변화에도 1 추가해주기
            changed_number += 1

    # 최종 결과를 answer에 넣어주기
    answer = [changed_number, delete_zero]

    return answer




