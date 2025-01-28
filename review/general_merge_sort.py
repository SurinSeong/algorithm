# 일반적인 병합 정렬
'''
- 종료조건 : 정렬할 리스트의 요소가 하나 이하면 정렬 필요 없음.
- 내부 과정 : 그룹을 나누어 각각 병합 정렬을 호출
    1) 중간을 기준으로 두 그룹으로 나눈다.
    2) 재귀 호출로 나눈 그룹을 정렬한다.
    3) 나눈 그룹을 하나로 묶는다.
    4) 아직 남아있는 자료들을 결과에 추가한다.
'''

def merge_sort(number_list):
    list_length = len(number_list)
    # 리스트 길이가 1 이하 이면 리스트 반환
    if list_length <= 1:
        return number_list
    # 리스트 길이가 2 이상일 경우
    middle = list_length // 2
    group1 = number_list[:middle]
    group2 = number_list[middle:]
    # 병합 정렬하기
    merge_sort(group1)
    merge_sort(group2)
    
    # 두 그룹을 하나로 병합하기
    # 인덱스 숫자를 하나씩 늘려가며 해당 위치에 숫자를 넣기
    idx1, idx2, list_idx = 0, 0, 0
    while idx1 < len(group1) and idx2 < len(group2):
        if group1[idx1] < group2[idx2]:
            print(f'group1 : {group1} | group2 : {group2}')
            number_list[list_idx] = group1[idx1]
            idx1 += 1
            list_idx += 1
            print(f'>>> {number_list}')
        else:
            print(f'group1 : {group1} | group2 : {group2}')
            number_list[list_idx] = group2[idx2]
            idx2 += 1
            list_idx += 1
            print(f'>>> {number_list}')
    
    # 아직 group1에 남은 숫자가 있다면
    while idx1 < len(group1):
        print(f'group1 : {group1} | group2 : {group2}')
        number_list[list_idx] = group1[idx1]
        idx1 += 1
        list_idx += 1
        print(f'>>> {number_list}')
        
    # 아직 group2에 남은 숫자가 있다면
    while idx2 < len(group2):
        print(f'group1 : {group1} | group2 : {group2}')
        number_list[list_idx] = group2[idx2]
        idx2 += 1
        list_idx += 1
        print(f'>>> {number_list}')
                                           
    
d = [6, 8, 3, 9, 10, 1, 2, 4, 7, 5]
merge_sort(d)
print(d)