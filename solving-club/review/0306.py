# 위치 찾기 함수

# 1. 매핑테이블 만들기

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    
    # 2. 시작 위치 찾기
    sx, sy = find_pos(arr)
    sy -= 55    # 암호의 길이가 56개이기 때문에 55를 빼준다.

    # 3. 7개씩 슬라이싱해서 매핑 테이블에서 암호 구하기 -> 리스트에 보관
    pwd = []
    for i in range(8):
        pwd.append(mapping_code.get(''.join(map(str, arr[sx][sy:sy+7]))))
        sy += 7
    
    # 4. 검증
    odd = pwd[0] + pwd[2] + pwd[4] + pwd[6]
    even = pwd[1] + pwd[3] + pwd[5] + pwd[7]
    
    if (odd*3 + even) % 10 == 0:    # 올바른 암호
        print(f'#{tc} {odd+even}')
    else:    # 올바르지 않은 암호
        print(f'#{tc} 0')