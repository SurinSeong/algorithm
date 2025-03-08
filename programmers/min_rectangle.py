"""
[최소 직사각형]
- 지갑 크기 정하기

[조건]
- 다양한 모양과 크기의 명함을 모두 수납
- 작아서 들고 다니기 편한 지갑

- 모든 명함의 가로 길이와 세로 길이를 나타내는 2차원 배열 : sizes
- 작은 지갑의 크기
"""
def solution(sizes):
    N = len(sizes)
    cards = [[0]*N for _ in range(2)]    # 가로와 세로 중 더 큰 값을 0번 행에 넣어줄 예정
    
    for i, size in enumerate(sizes):
        w, h = size[0], size[1]
        if w > h:
            cards[0][i], cards[1][i] = w, h
        else:
            cards[0][i], cards[1][i] = h, w
    
    max_w, max_h = max(cards[0]), max(cards[1])
    
    answer = max_w * max_h
    
    return answer


sizes = [[60, 50], [30, 70], [60, 30], [80, 40]]
print(solution(sizes))