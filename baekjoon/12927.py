# 전구 N개 1~N
# 모든 전구 끄기
# 스위치 N개 -> i번 스위치 : i의 배수인 전구 상태 반전
# 모든 전구를 끄기 위해 스위치 몇번 누를지, 끌 수 없다면 -1

"""
4
YYYYYY
YNYNYNYNY
NNNNNNNNNN
YYYNYYYNYYYNYYNYYYYN
"""

# 리스트 형태로 입력받기
lights = list(input())

# 스위치 조작 횟수
total = 0
# 나누기 할 변수
divisor = 1
# 가장 첫번째 Y의 위치
small_loc = 1

while True:
    # 모든 요소가 N이라면
    if list(set(lights)) == ['N']:
        # 끝
        break

    # 가장 첫 번째 Y 구하기
    for i, light in enumerate(lights):
        if light == 'Y':
            small_loc = i+1
            break

    # 만약 Y인 인덱스+1이 divisor보다 작다면
    if small_loc < divisor:
        # 찾을 수 없음
        total = -1
        # 끝내기
        break

    # 아니라면
    else:
        # 업데이트
        divisor = small_loc

    # 온오프 바꿔주기
    for i, light in enumerate(lights):
        # 나눠지지 않으면
        if (i+1) % divisor:
            continue
        # 나눠지면
        if light == 'Y':
            lights[i] = 'N'
        else:
            lights[i] = 'Y'

    total += 1

print(total)