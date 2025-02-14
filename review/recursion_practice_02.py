# 숫자 n개 중에서 최댓값 찾기
# 입력 : 숫자가 n개 들어있는 리스트
# 출력 : 숫자 n개 중 최댓값

def find_max_number(number_list):
    if len(number_list) == 1:
        return number_list[0]
    else:
        # 가장 마지막 수를 빼내서 반환
        max_number = number_list.pop()
        if max_number >= number_list[-1]:
            # 더 작은 것 삭제
            number_list.pop()
            # 더 큰 것 넣어주기
            number_list.append(max_number)
            return find_max_number(number_list)
        
        else:
            return find_max_number(number_list)
        

print(find_max_number([1, 3, 10, 9, 7]))

# 다른 방식으로 해보기
# 입력 : 리스트와 리스트 길이
# 출력 : 최댓값

def find_max_number(number_list, list_length):
    # 리스트 길이가 1 이라면
    if list_length == 1:
        # 요소 하나의 값 반환
        return number_list[0]
    # 1 이상이라면
    else:
        max_number = find_max_number(number_list, list_length-1)
        if max_number > number_list[list_length-1]:
            return max_number
        else:
            return number_list[list_length-1]
        
# ==> 이거 글로 써보면서 해보기