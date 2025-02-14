# 순차 탐색
# 주어진 리스트에 특정한 값이 있는지를 찾아 그 위치를 돌려주는 알고리즘
# 리스트에 찾는 값이 없다면 -1을 돌려준다.
'''
- 순차 탐색 : 리스트 안에 있는 원소를 하나씩 순차적으로 비교하면서 탐색
- 리스트에 있는 첫 번째 자료부터 하나씩 비교하면서 같은 값이 나오면 그 위치를 결과로 돌려준다.
- 리스트 끝까지 찾아도 같은 값이 나오지 않으면 -1을 돌려준다.
'''

# 주어진 리스트 : [17, 92, 18, 33, 58, 5, 33, 42]
# 특정 값 : (18, 33, 900)

def search_number(number_list, target):
    for i in range(len(number_list)):
        if number_list[i] == target:
            return i
    else:
        return -1
    


v = [17, 92, 18, 33, 58, 7, 33, 42]
    
print(search_number(v, 18))
print(search_number(v, 20))


'''
순차 탐색의 계산 복잡도는 O(n)
'''