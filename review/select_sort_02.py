# 일반적인 선택 정렬 알고리즘
# 입력 : 리스트
# 출력 : 없음.

def select_sort(number_list):
    for i in range(0, len(number_list)-1):
        # 일단 해당 인덱스를 최솟값의 인덱스라고 설정
        min_idx = i
        # i번 위치부터 끝까지 자료값 중 최솟값의 위치를 찾는다.
        for j in range(i+1, len(number_list)):
            # 만약 min_idx의 숫자값보다 j의 숫자값이 더 작다면
            if number_list[j] < number_list[min_idx]:
                # min_idx를 j로 바꿔준다.
                min_idx = j
                
        # 위치 바꿔주기        
        number_list[i], number_list[min_idx] = number_list[min_idx], number_list[i]
        

d = [2, 4, 5, 1, 3]
select_sort(d)
print(d)


'''
이 방법은 두 수를 비교하는 방법으로 진행된다.
계산 복잡도 : O(n^2)
=> 비교 횟수가 입력 크기의 제곱에 비례
'''