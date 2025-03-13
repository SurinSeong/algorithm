"""
[최대 상금]
- 우승자 : 주어진 숫자판(최대 6자릿수)들 중 두 개를 선택해서 정해진 횟수만큼 위치 교환 가능
- 반드시 횟수만큼 교환 (최대 10번)이 이루어져야함.
- 오른쪽 끝에서부터 1원 -> 왼쪽으로 갈수록 10의 배수만큼 커진다.
"""
def make_max_money(cnt):
    global answer

    state = (int(''.join(number_list)), cnt)    # 현재 교환 상태 체크를 위해 cnt와 함께 visited에 넣어준다.
    if state in visited:
        return
    visited.add(state)

    if cnt == rotation:
        answer = max(answer, int(''.join(number_list)))
        return

    for i in range(N-1):
        for j in range(i+1, N):
            number_list[i], number_list[j] = number_list[j], number_list[i]
            make_max_money(cnt+1)
            number_list[i], number_list[j] = number_list[j], number_list[i]


# 테스트 케이스 개수
T = int(input())

for tc in range(1, T+1):
    # 숫자판, 교환횟수
    numbers, rotation = map(int, input().split())
    number_list = [n for n in str(numbers)]

    N = len(number_list)    # 숫자판 길이

    # 최종 상금
    answer = 0
    visited = set()

    make_max_money(0)

    print(f'#{tc} {answer}')
