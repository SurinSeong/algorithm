# 최대 수익 알고리즘
'''
어떤 주식에 대해 특정 기간 동안의 가격 변화가 주어졌을 때,
그 한 주를 한 번 사고팔아 얻을 수 있는 최대 수익을 계산하는 알고리즘.
'''

# 각 날의 주식 가격 리스트
stocks = [10300, 9600, 9800, 8200, 7800, 8300, 9500, 9800, 10200]

# 두 번째 방법 : 한 번 반복으로 최대 수익 찾기


def find_max_profit(stock_list):
    # 최대 수익을 저장하는 변수
    max_profit = 0
    
    # 지금까지의 최저 주가를 저장하는 변수
    min_stock = stock_list[0]   # 첫째 날의 주가
    
    # 둘째 날의 주가 부터 마지막 날의 주가까지 반복
    for i in range(1, len(stock_list)):
        # 그날의 주가에서 최저 주가를 뺀 값이 현재 최대 수익보다 크면
        if max_profit < stock_list[i] - min_stock:
            # 최대 수익 값을 그 값으로 고침
            max_profit = stock_list[i] - min_stock
        
        # 그날의 주가가 최저 주가보다 낮으면
        if stock_list[i] < min_stock:
            # 최저 주가 값을 그날의 주가로 고침
            min_stock = stock_list[i]
            
        # print(f'현재 주가 : {stock_list[i]}\n최대 수익 : {max_profit}\n지금까지의 최저 주가 : {min_stock}\n')
            
    return max_profit


print(find_max_profit(stocks))