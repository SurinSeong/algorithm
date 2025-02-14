# 병합 정렬 >> 리스트 안의 자료를 작은 수부터 큰 수 순서로 배열하는 정렬 알고리즘
# 재귀 호출을 사용해보기
# 다시 | 다시 | 다시 | 다시 | 다시
'''
Merge Sort
1) 열 명의 학생을 다섯 명씩 두 조로 나누어 그 안에서 키 순서로 줄을 서라고 함.
2) 각 줄의 맨 앞의 학생 중 더 작은 학생을 뽑아 최종 결정 줄을 세운다.
3) 이 과정을 계속해서 한다.
'''
'''
재귀 호출의 세 가지 요건
1) 함수 안에서 자기 자신을 다시 호출
2) 인자로 주어지는 입력의 크기가 작아진다.
3) 특정 종료 조건이 만족되면 재귀 호출을 종료
'''


# 쉽게 설명한 병합 정렬 알고리즘
def merge_sort(number_list):
    # 리스트 안의 요소의 개수가 1 또는 0 일 경우
    if len(number_list) <= 1:
        return number_list
    # 정렬이 필요한 경우
    else:
        middle = len(number_list) // 2
        
        # 두 그룹으로 나눈다.
        # 두 그룹도 병합 정렬 방식으로 순서를 맞춰준다.
        group1 = merge_sort(number_list[:middle])
        group2 = merge_sort(number_list[middle:])
        
        # 빈 결과 리스트 생성
        result = []
        
        # 두 리스트를 합치는 과정 반복
        # 1. 두 그룹의 요소가 모두 존재할 경우
        while group1 and group2:
            if group1[0] < group2[0]:
                print(f'group1 >> {group1} | group2 >> {group2}')
                result.append(group1.pop(0))
                print(f'>>> {result}')
            else:
                print(f'group1 >> {group1} | group2 >> {group2}')
                result.append(group2.pop(0))
                print(f'>>> {result}')
                
                
        # 2. 하나의 그룹이 모두 사라졌을 경우
        while group1:
            print(f'group1 >> {group1} | group2 >> {group2}')
            result.append(group1.pop(0))
            print(f'>>> {result}')
        while group2:
            print(f'group1 >> {group1} | group2 >> {group2}')
            result.append(group2.pop(0))
            print(f'>>> {result}')
            
    return result


d = [6, 8, 3, 9, 10, 1, 2, 4, 7, 5]
print(merge_sort(d))