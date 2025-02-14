# 일반적인 삽입 알고리즘 => 계산 복잡도 : O(n^2)
def insert_sort(number_list):
    # 인덱스 1부터 끝까지 반복
    for i in range(1, len(number_list)):
        # 타겟 숫자 설정
        target = number_list[i]
        print(target, end=' >>> ')
        
        # 타겟 숫자의 왼쪽 인덱스를 j로 저장
        j = i - 1
        # 리스트의 j에 있는 값과 target을 비교해 적절한 위치 찾기
        # j가 0 이상이고, target이 j 위치의 값보다 작으면
        while (j >= 0) and (number_list[j] > target):
            # j에 있는 값을 한칸 뒤로 옮겨주기
            number_list[j+1] = number_list[j]
            j -= 1
        # 그렇지 않으면 target의 위치를 옮겨줌.
        number_list[j+1] = target
        print(number_list)
        
        
d = [2, 4, 5, 1, 3]
insert_sort(d)