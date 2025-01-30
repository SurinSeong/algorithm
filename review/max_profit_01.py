# 최대 수익 알고리즘
'''
어떤 주식에 대해 특정 기간 동안의 가격 변화가 주어졌을 때,
그 한 주를 한 번 사고팔아 얻을 수 있는 최대 수익을 계산하는 알고리즘.
'''

# 각 날의 주식 가격 리스트
stocks = [10300, 9600, 9800, 8200, 7800, 8300, 9500, 9800, 10200]

# 첫 번째 방법 : 가능한 모든 경우 비교하기 => 계산 복잡도 : O(n^2)
# 주식을 살 수 있는 모든 날과 팔 수 있는 모든 날의 주가를 비교해서 가장 큰 수익을 찾는 것

def find_max_profit(stock_list):
    '''
    주어진 주식 가격을 보고 얻을 수 있는 최대 수익을 구하는 알고리즘
    입력 : 주식 가격의 변화값
    출력 : 한 주를 한 번 사고팔아 얻을 수 있는 최대 수익 값
    '''
    # 주식 가격 리스트 저장
    n = len(stock_list)
    
    max_profit = 0
    
    for i in range(0, n-1):
        for j in range(i+1, n):
            # i날 산 주식을 j날에 판다면
            if max_profit < stock_list[j] - stock_list[i]:
                max_profit = stock_list[j] - stock_list[i]
    
    return max_profit


print(find_max_profit(stocks))