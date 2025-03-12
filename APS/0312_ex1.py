# 주사위 3개를 던져 합이 10 이하인 경우는 몇개?
# 종료 조건 : 3번 던지기
# 나올 수 있는 범위 : 1 ~ 6

path = []
result = 0

def recur(cnt, total):
    global result

    # 이미 10을 넘으면 더이상 볼필요 없음.
    if total > 10:
        return

    # # 종료 조건 방법 1
    if cnt == 3:
    #     # 합이 10 이하인 것은 몇 개일까? ==> 주사위 하나 뽑을 때마다 합을 누적시킨다면?
    #     if sum(path) <= 10:    # path 길이만큼 반복되기 때문에 비효율 (O(n))
    #         result += 1
    #     return

        # 주사위 하나 뽑을 때마다 합을 누적
        if total <= 10:
            result += 1
            print(path)

        return

    for num in range(1, 7):    # 주사위 숫자 범위 만큼
        path.append(num)
        recur(cnt + 1, total + num)    # 주사위 결과를 더해서 전달!
        path.pop()

recur(0, 0)