# 일반적인 삽입 정렬 알고리즘을 사용해 리스트 [2, 4, 5, 1, 3]을 정렬하는 과정 출력
def general_insert_sort(number_list):
    for i in range(1, len(number_list)):
        target = number_list[i]
        print(target, end=' >>> ')
        j = i - 1
        while (j >= 0) and (target > number_list[j]):
            number_list[j+1] = number_list[j]
            j -= 1
        number_list[j+1] = target
        print(number_list)
        
d = [2, 4, 5, 1, 3]
general_insert_sort(d)

# 오름차순, 내림차순 둘다 가능하도록
def general_insert_sort(number_list, reverse=False):
    if reverse:
        print('=== 내림차순 ===')
        for i in range(1, len(number_list)):
            target = number_list[i]
            j = i - 1
            while (j >= 0) and (target > number_list[j]):
                number_list[j+1] = number_list[j]
                j -= 1
            number_list[j+1] = target
    else:
        print('=== 오름차순 ===')
        for i in range(1, len(number_list)):
            target = number_list[i]
            j = i - 1
            while (j >= 0) and (target < number_list[j]):
                number_list[j+1] = number_list[j]
                j -= 1
            number_list[j+1] = target
    
    return number_list
            
            
print(general_insert_sort(d, False))