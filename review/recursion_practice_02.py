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