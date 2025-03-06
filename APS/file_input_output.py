import sys
sys.stdin = open('./input/input.txt', 'r')
# sys.stdout = open('output.txt' 'w')    # 해당 파일을 쓰기 모드로 열겠다.

"""
stdin : standard input (표준 입력)
    input.txt를 읽기 모드로 열겠다.
    'r' : 읽기 모드

테스트 케이스를 수정하며 디버깅하기 위해 사용함.
아웃풋도 비교가능함.
"""

a, b = map(int, input().split())
print(a, b)