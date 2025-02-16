# baby_gin_game
def baby_gin(arr, n=10):
    i = 1
    cnt = 0
    
    while i < n:
        # 111
        if arr[i] == 3:
            cnt += 1
            arr[i] -= 3
        
        # 123
        if arr[i] == 1 and arr[i+1] == 1 and arr[i+2] == 1:
            cnt += 1
            arr[i] -= 1
            arr[i+1] -= 1
            arr[i+2] -= 1
        
        i += 1
    
    if cnt == 2:
        return True
    return False


# 테스트 케이스 수
T = int(input())

for test_case in range(1, T+1):
    cards = list(map(int, input()))
    temp = [0]*10
    
    for card in cards:
        temp[card] += 1
    
    result = baby_gin(temp)
    
    print(f'#{test_case} {result}')