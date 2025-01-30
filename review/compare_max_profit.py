# 방법 1, 방법 2의 알고리즘 계산 속도 비교

import time
import random

from max_profit_01 import find_max_profit as slow_way
from max_profit_02 import find_max_profit as fast_way

def compare_max_profit(n):
    '''
    최대 수익 문제를 푸는 두 알고리즘의 계산 속도 비교하기
    - 최대 수익 문제를 O(n^2)과 O(n)으로 푸는 알고리즘을 각각 수행
        => 걸린 시간 출력 및 비교
    '''
    # 테스트 자료 만들기 (5000부터 20000까지의 난수 생성 -> 주가로 사용한다.)
    a = []
    
    for i in range(0, n):
        a.append(random.randint(5000, 20000))
        
        # O(n^2) 테스트
        start = time.time() # 계산 시작 직전 시각을 기억한다.
        mps = slow_way(a)
        end = time.time() # 계산 시작 직후 시각을 기억한다.
        time_slow = end - start # 두 시각을 빼면 계산에 걸린 시간!
        
        # O(n) 테스트
        start = time.time() # 계산 시작 직전 시각을 기억한다.
        mpf = fast_way(a)
        end = time.time() # 계산 시작 직후 시각을 기억한다.
        time_fast = end - start # 두 시각을 빼면 계산에 걸린 시간!
        
        # 결과 출력
        print(n, mps, mpf) # 입력 크기, 각각 알고리즘이 계산한 최대 수익 값
        m = 0 # slow와 fast의 수행 시간 비율을 저장할 변수
        
        if time_fast > 0:
            m = time_slow / time_fast
            
        print(f'\n{n} {time_slow:.5f} {time_fast:.5f} {m}')
    

compare_max_profit(100)