# 처리할 대상 범위에서 최솟값을 찾아 그 값과 범위의 맨 앞에 있는 값을 서로 바꾸는 과정을 반복
# 이미 정렬이 끝난 부분과 앞으로 처리될 대상 범위 사이에 세로 선을 넣어 구분한다.
def select_sort(number_list):
    for i in range(len(number_list)-1):
        min_idx = i
        
        for j in range(i, len(number_list)):
            if number_list[min_idx] > number_list[j]:
                min_idx = j
                
        number_list[i], number_list[min_idx] = number_list[min_idx], number_list[i]
        print(number_list)
    

d = [2, 4, 5, 1, 3]
select_sort(d)

# 내림차순
def select_sort(number_list):
    for i in range(len(number_list)-1):
        max_idx = i
        for j in range(i, len(number_list)):
            if number_list[max_idx] < number_list[j]:
                max_idx = j
                
        number_list[i], number_list[max_idx] = number_list[max_idx], number_list[i]
        print(number_list)
        
 
d = [2, 4, 5, 1, 3]
select_sort(d)

# 매개 변수 추가해서 오름차순, 내림차순 모두 가능할 수 있도록 만들어보기
def select_sort(number_list, reverse=False):
    # 오름차순
    if not reverse:
        print('=== 오름차순 ===')
        for i in range(len(number_list)-1):
            idx = i
            for j in range(i, len(number_list)):
                if number_list[idx] > number_list[j]:
                    idx = j
                    
            number_list[i], number_list[idx] = number_list[idx], number_list[i]
            print(number_list)
        
    # 내림차순
    else:
        print('=== 내림차순 ===')
        for i in range(len(number_list)-1):
            idx = i
            for j in range(i, len(number_list)):
                if number_list[idx] < number_list[j]:
                    idx = j
        
            number_list[i], number_list[idx] = number_list[idx], number_list[i]
            print(number_list)
        

d = [2, 4, 5, 1, 3]
select_sort(d, reverse=True)
print()

