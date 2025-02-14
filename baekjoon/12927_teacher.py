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

