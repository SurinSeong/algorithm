# 퀵 정렬
'''
그룹을 둘로 나눠 재귀 호출을 하는 방식은 병합 정렬과 같지만, 그룹을 나눌 때 미리 기준과 비교해서 나눈다.
=> 먼저 기준과 비교해서 그룹을 나눈 다음, 각각 재귀 호출을 이용해 합친다.

< 예시 >
1) 학생 열 명 중 기준이 될 사람을 한 명 뽑는다.
2) 기준을 가운데에 세운다.
3) 기준과 비교해 작으면 왼쪽, 크면 오른쪽으로 보낸다. (오름차순)
'''

def quick_sort(number_list):
    # 리스트의 길이가 하나 이하이면 바로 반환
    if len(number_list) <= 1:
        return number_list
    # 리스트 길이가 2 이상이면 퀵 정렬 시작
    # 새로운 리스트 두개 만들기
    small_group, big_group = [], []
    
    # 기준 설정하기
    pivot = number_list.pop()
    print(f'pivot : {pivot}')
    
    # number list에 숫자가 없어지기 전까지, 겹치는 숫자 없음.
    for i in range(len(number_list)):
        print(f'LEFT : {small_group} | RIGHT : {big_group}')
        
        if number_list[i] > pivot:
            big_group.append(number_list[i])
        else:
            small_group.append(number_list[i])
            
        print(f'    ↓\nLEFT : {small_group} | RIGHT : {big_group}')
    
    print(f'FINAL >>> LEFT {small_group} PIVOT {pivot} RIGHT {big_group}\n')
    return quick_sort(small_group) + [pivot] + quick_sort(big_group)


d = [6, 8, 3, 9, 10, 1, 2, 4, 7, 5]
print(quick_sort(d))