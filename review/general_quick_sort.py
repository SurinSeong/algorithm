# 일반적인 퀵 정렬 알고리즘
def in_quick_sort(number_list, start, end): # 리스트의 어디서부터(start) 어디까지(end)가 정렬 대상인지
    if end - start <= 0:
        return number_list
    # 기준 값을 정하고 기준 값에 맞춰 리스트 안에서 각 자료의 위치를 맞춘다.
    pivot = number_list[end] # 편의상 리스트의 마지막 값을 기준 값으로 정한다.
    i = start
    
    for j in range(start, end):
        if number_list[j] <= pivot:
            number_list[i], number_list[j] = number_list[j], number_list[i]
            i += 1
            
    number_list[i], number_list[end] = number_list[end], number_list[i]
    
    # 재귀 호출
    in_quick_sort(number_list, start, i-1)
    in_quick_sort(number_list, i+1, end)
    
    
# 리스트 전체를 대상으로 재귀 호출 함수 호출
def quick_sort(number_list):
    in_quick_sort(number_list, 0, len(number_list)-1)
    

d = [6, 8, 3, 9, 10, 1, 2, 4, 7, 5]
quick_sort(d)
print(d)
    