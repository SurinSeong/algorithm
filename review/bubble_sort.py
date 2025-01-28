# 거품 정렬
'''
< 예시 >

1) 맨 앞에서부터 뒤로 이동하면서 이웃한 앞뒤 학생의 키를 서로 비교
    ex) 앞에 있는 학생의 키가 바로 뒤에 있는 학생보다 크면 두 학생의 자리를 서로 바꿈.
2) 선생님이 계속 뒤로 이동하면서 이웃한 앞뒤 학생의 키를 비교해서 필요하면 앞뒤 학생의 위치를 서로 바꾼다.
3) 모든 학생이 키 순서대로 줄을 설 때까지 이 과정을 반복한다.
    (줄의 끝까지 확인하는 동안 자리를 바꾼 적이 한 번도 없으면 모든 학생이 순서대로 줄을 선 것으로 판단.)

< 특징 >
- 최선의 계산 복잡도 : O(n) / 일반적인 입력에 대한 거품 정렬의 계산 복잡도 : O(n^2)
'''


def bubble_sort(number_list, reverse=False):
    '''
    Bubble Sort
    - In number_list, only unique numbers
    '''
    # 리스트의 길이가 1 이하이면 그대로 반환
    if len(number_list) <= 1:
        return number_list
    # 리스트의 길이가 2 이상이면
    
    # 반복횟수 확인
    n = 1
    
    while True:
        print(f'=== {n} 번째 시도 ===')
        
        # 변경했는지 확인하는
        flag = False
        
        for i in range(len(number_list)-1):
            
            print(number_list, end=' >> ')
            
            # 오름차순일 때
            if not reverse:
                if number_list[i] > number_list[i+1]:
                    # 앞뒤의 위치 바꾸기
                    number_list[i], number_list[i+1] = number_list[i+1], number_list[i]
                    flag = True
                    
            # 내림차순일 때
            else:
                if number_list[i] < number_list[i+1]:
                    # 앞뒤의 위치 바꾸기
                    number_list[i], number_list[i+1] = number_list[i+1], number_list[i]
                    flag = True
                
            print(number_list)
        
        # 반복 횟수 증가
        n += 1
                
        if not flag:
            print('정렬 완료')
            return number_list
        


d = [2, 4, 5, 1, 3]
print(bubble_sort(d, reverse=True))

