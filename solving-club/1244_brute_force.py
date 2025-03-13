"""
[최대 상금]
- 우승자 : 주어진 숫자판(최대 6자릿수)들 중 두 개를 선택해서 정해진 횟수만큼 위치 교환 가능
- 반드시 횟수만큼 교환 (최대 10번)이 이루어져야함.
- 오른쪽 끝에서부터 1원 -> 왼쪽으로 갈수록 10의 배수만큼 커진다.
"""
def get_comb(cnt, comb):
    if cnt == 2:
        print(comb)
        return

    for i in range(N):
        get_comb(cnt+1, comb+[number_list[i]])



# 테스트 케이스 개수
T = int(input())

for tc in range(1, T+1):
    # 숫자판, 교환횟수
    numbers, rotation = map(int, input().split())
    number_list = [int(n) for n in str(numbers)]

    N = len(number_list)    # 숫자판 길이

    # 최종 상금
    answer = 0

    # 교환 가능한 경우의 수 찾기
    # 1. 가장 큰 수 찾기
    max_num = max(number_list)
    max_idx_list = []    # 가장 큰수의 인덱스 넣는 곳

    for i in range(1, len(number_list)):
        if max_num == number_list[i]:
            max_idx_list.append(i)

    not_max = 0

    # 인덱스가 0인 자리에 가장 큰 수가 들어가는 것이 맞음.
    while rotation:

        if number_list[not_max] == max_num:    # 가장 큰수이면
            not_max += 1


        if not_max == 0:
            number_list[-1], number_list[-2] = number_list[-2], number_list[-1]
            rotation -= 1
            continue

        not_max -= 1
        # 가장 마지막 인덱스
        mi = max_idx_list.pop()
        if mi > not_max:
            number_list[not_max], number_list[mi] = number_list[mi], number_list[not_max]
            rotation -= 1

    answer = ''.join(map(str, number_list))

    print(f'#{tc} {answer}')