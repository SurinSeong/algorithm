# 20:30 ~

"""
[로봇 청소기]
- 답 : 청소하는 영역의 개수
- 방 : N x M (벽 or 빈 칸)
- 청소기 : 상하좌우

[청소기 작동법]
1. 현재 칸이 청소 전이면 청소
2. 현재 칸의 주변 4칸 중 청소 전인 칸이 없다면
    1) 보고 있는 방향 유지 & 후진 가능이면(벽이 없다면) 후진하고 1번(현재 칸)으로
    2) 후진 못하면 중지
3. 청소 전인 칸이 있다면
    1) 반시계 회전 (좌 -> 상)
    2) 바라보는 칸이 청소되지 않았다면 전진
    3) 1번
"""

"""
3 3
1 1 0
1 1 1
1 0 1
1 1 1
11 10
7 4 0
1 1 1 1 1 1 1 1 1 1
1 0 0 0 0 0 0 0 0 1
1 0 0 0 1 1 1 1 0 1
1 0 0 1 1 0 0 0 0 1
1 0 1 1 0 0 0 0 0 1
1 0 0 0 0 0 0 0 0 1
1 0 0 0 0 0 0 1 0 1
1 0 0 0 0 0 1 1 0 1
1 0 0 0 0 0 1 1 0 1
1 0 0 0 0 0 0 0 0 1
1 1 1 1 1 1 1 1 1 1
"""
# # 바라보는 위치 바꾸기
# def change_eye():
#     pass


# 2번 & 3번
def check_status(ci, cj, cur_eye):
    for di, dj in delta:
        ni, nj = ci+di, cj+dj
        if 0 <= ni < N and 0 <= nj < M:    # 배열 안에 있다면
            if rooms[ni][nj] == 0:    # 청소 전인 칸이라면
                break    # 청소 전인 칸 찾았다!
    # 청소 전인 칸을 못 찾았다면
    else:
        # 뒤로 갈 수 있는지 확인
        bi, bj = ci-delta[cur_eye][0], cj-delta[cur_eye][1]
        if rooms[bi][bj] != 1:    # 벽이 아니라면
            ci, cj = bi, bj    # 후진
            return ci, cj, cur_eye
        else:
            return -1, -1, -1   # 움직이지 못함.
                
    # 청소 전인 칸을 찾았다면         
    cur_eye = (cur_eye+3) % 4    # 반시계로 돌리기
    if rooms[ci+delta[cur_eye][0]][cj+delta[cur_eye][1]] == 0:    # 청소 전이라면
        ci, cj = ci+delta[cur_eye][0], cj+delta[cur_eye][1]    # 칸 이동
        
    return ci, cj, cur_eye
    


# 청소하기
def clean_the_room(ci, cj, cur_eye):
    cnt = 0
    while True:    
        # 1번
        if rooms[ci][cj] == 0:
            rooms[ci][cj] = -1    # 청소 표시
            cnt += 1    # 영역 + 1
            
            new_ci, new_cj, new_eye = check_status(ci, cj, cur_eye)    # 상태 확인하기
            if new_ci == -1:
                break    # 작업 중지
            else:
                ci, cj, cur_eye = new_ci, new_cj, new_eye    # 장소 업데이트, 보는 방향 업데이트
            
        elif rooms[ci][cj] == -1:    # 이미 청소가 되었다면
            new_ci, new_cj, new_eye = check_status(ci, cj, cur_eye)
            if new_ci == -1:
                break
            else:
                ci, cj, cur_eye = new_ci, new_cj, new_eye
        
    return cnt

# 테스트 케이스 개수
T = int(input())

for tc in range(1, T+1):
    # 방의 크기
    N, M = map(int, input().split())
    # 시작 좌표, 방향 (0 : 북, 1 : 동, 2: 남, 3: 서)
    si, sj, eye = map(int, input().split())
    # 방의 상태 (0 : 청소 전 / 1 : 벽)
    rooms = [list(map(int, input().split())) for _ in range(N)]
    
    delta = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    
    answer = clean_the_room(si, sj, eye)
    
    print(f'#{tc} {answer}')
    