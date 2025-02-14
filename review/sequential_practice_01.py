# 리스트에 찾는 값이 나오는 모든 위치를 리스트로 돌려주는 탐색 알고리즘
# 찾는 값이 없다면 빈 리스트 반환
def find_all_indexes(number_list, target):
    
    index_list = []
    
    for i in range(len(number_list)):
        if target == number_list[i]:
            index_list.append(i)
    
    return index_list


v = [17, 92, 18, 33, 58, 7, 33, 42]

print(find_all_indexes(v, 18))
print(find_all_indexes(v, 33))
print(find_all_indexes(v, 900))

# ==> 계산 복잡도 : O(n)