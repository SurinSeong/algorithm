"""
[정식이의 은행업무]
- 2진수 / 3진수
    - 각각에서 단 한자리만 잘 못 기억하고 있음.
"""
def change_binary():
    change_list = []

    for i in range(len(binary)):
        if binary[i] == '1':
            binary[i] = '0'
        else:
            binary[i] = '1'



# 테스트 케이스 개수
T = int(input())

for tc in range(1, T+1):
    # 2진수 표현
    binary = list(input())
    # 3진수 표현
    ternary = list(input())

    answer = 0



    print(f'#{tc} {answer}')