"""
0b110 이 주어지면, BC 출력하는 함수 (비트연산 활용)
- 0x1과 AND 연산을 한다.
- shift 연산자를 이용해 다음 비교할 자리로 넘어간다. (>>=)
"""
# 부분집합을 얻는 함수
def get_subset(x):    # x : 부분집합의 자리를 나타내는 이진수
    print(f'target = {x}', end=' / ')

    for i in range(N):    # 각각의 원소를 확인하기

        if x & 0x1:    # 각 자리의 원소가 포함되어 있다면 (0x1 : 이진수 1, 0 확인인 것을 나타내기 위해서 = 비트 연산임을 명시)
            print(arr[i], end='')

        x >>= 1    # 다음 이진수로 넘어간다. (맨 우측 비트 삭제)



arr = ['A', 'B', 'C']

N = len(arr)

for target in range(1 << N):    # 전체 부분집합 확인하기
    get_subset(target)
    print()