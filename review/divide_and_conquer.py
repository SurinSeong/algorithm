'''
분할 정복 (divide and conquer) : 큰 문제를 작은 문제로 나눠서 푸는 방법
(입력 크기가 커서 풀기 어려웠던 문제도 반복해서 잘게 나누다보면 굉장히 쉬운 문제가 되는 원리)
계산 복잡도 : O(n*log(n))
=> 정렬해야 할 자료의 개수가 많을수록 병합 정렬이 선택 정렬이나 삽입 정렬보다 훨씬 더 빠른 성능 발휘
'''
# 분할 정복 알고리즘 작성하기 (오름차순이 기본)
def divide_and_conquer(number_list, reverse=False):
    # 숫자 리스트의 요소 개수
    list_length = len(number_list)
    # 만약 요소의 개수가 하나 이하이면 리스트 그대로 반환
    if list_length <= 1:
        return number_list
    
    # 요소 개수가 2개 이상인 경우
    # 두 그룹으로 나누기 위해 중간 숫자 저장
    middle = list_length // 2
    # 두 그룹도 분할 정복 방식으로 정렬되어야 함.
    group1 = divide_and_conquer(number_list[:middle])
    group2 = divide_and_conquer(number_list[middle:])
    
    # 새로 정렬한 리스트
    result = []
    
    # 두 그룹을 분할 정복 하는 알고리즘 작성
    # 두 그룹의 요소가 다 있는 경우
    while group1 and group2:
        # 오름차순일 경우
        if not reverse:
            # 두 그룹 중 첫 번째 요소 비교하기
            if group1[0] < group2[0]:
                # 첫 번째 요소 빼서 새로운 리스트에 담기
                result.append(group1.pop(0))
            else:
                result.append(group2.pop(0))
        
        # 내림차순일 경우
        else:
            # 두 그룹 중 첫 번째 요소 비교하기
            if group1[0] > group2[0]:
                # 첫 번째 요소 빼서 새로운 리스트에 담기
                result.append(group1.pop(0))       
            else:
                result.append(group2.pop(0))
                
    # 하나의 그룹의 요소만 존재하는 경우
    while group1:
        result.append(group1.pop(0))
        
    
    while group2:
        result.append(group2.pop(0))
            
    return result
        
    
d = [6, 8, 3, 9, 10, 1, 2, 4, 7, 5]
print(divide_and_conquer(d))
