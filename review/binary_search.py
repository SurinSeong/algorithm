# 이분 탐색
'''
자료가 크기 순서대로 **정렬된 리스트**에서 특정한 값이 있는지 찾아 그 위치를 돌려주는 알고리즘.
리스트에 찾는 값이 없으면 -1을 돌려준다.
    - 리스트 자료가 순서대로 정렬되어 있기 때문에 더 빠른 탐색 가능
    - 값을 비교할 때마다 찾는 값이 있을 범위를 절반씩 좁히면서 탐색
    - 계산 복잡도 : O(n*log(n))
    
ex)
    1) 책의 중간 끔을 펼쳐 쪽 수를 확인
    2) 찾고자 하는 쪽 수보다 작으면 펼친 곳의 뒤쪽을 펼친다. / 찾고자 하는 쪽 수보다 크면 펼친 곳의 앞쪽을 펼친다.
    3) 이렇게 찾다가 원하는 쪽 수와 가까워지면 하나씩 넘기며 찾아간다.
'''


# 이분 탐색으로 정렬된 리스트에서 특정 값의 위치 찾기
def binary_search(number_list, target):
    # 찾고 있는 범위 시작과 끝 위치 설정
    start = 0
    end = len(number_list)-1
    
    # 아직 찾을 수 있는 범위가 존재한다면 반복
    while (end - start) >= 0:
        
        # 리스트의 중간 위치를 찾는다.
        middle = (start + end) // 2
        print(f'{middle} >> {number_list[middle]}')
        
        # 같다면
        if number_list[middle] == target:
            print(f'{target} >> 발견!')
            return middle
        
        # target이 작다면
        elif number_list[middle] > target:
            end = middle - 1
            
        # target이 크다면
        else:
            start = middle + 1
    
    # 값이 없다면
    else:
        print(f'{target} >> 해당 리스트에 존재하지 않음.')
        return -1
    

numbers = [1, 4, 9, 16, 25, 36, 49, 64, 81]
binary_search(numbers, 40)