# 삽입 정렬
# 리스트 안의 자료를 작은 수부터 큰 수 순서로 배열하는 정렬 알고리즘
'''
1. 학생이 열 명 모인 운동장
2. 제일 앞에 있던 학생에게 나와서 줄 서라고 함. (9명이 남음.)
3. 다음 친구에게 줄을 서라고 함.
4. 다음 친구가 알아서 앞에 설지, 뒤에 설지 판단함.
5. 같은 방식으로 계속한다.
'''
# 리스트에서 v가 들어가야 할 위치를 돌려주는 함수
def find_idx(number_list, target):
    # 첫 번째 수부터 돌아가며 확인
    for i in range(len(number_list)):
        # 만약 타겟 숫자가 해당 인덱스의 숫자보다 작으면
        if target < number_list[i]:
            # 타겟 숫자가 해당 인덱스 숫자 앞에 놓여야 함.
            return i
    # 다 끝내도 타겟 숫자가 모든 숫자보다 작지 않다면
    else:
        # 맨 뒤로 보낸다.
        return len(number_list)
    
    
d = [2, 4, 5, 1, 3]
print(find_idx(d, 3))


# 위의 함수를 이용해 삽입 정렬 알고리즘 만들기 => 계산 복잡도 : O(n)
def insert_sort(number_list):
    # 삽입 정렬을 이용해 최종적으로 만들어지는 리스트
    result = []
    # 리스트 길이가 0이 되기 전까지
    while True:
        if len(number_list) > 0:
            # 첫 번째 숫자를 뺴내서 저장
            target = number_list.pop(0)
            # result의 어디에 들어가야 할지 판단 -> 위의 find_idx 함수를 이용
            target_idx = find_idx(result, target)
            print(target_idx)
            # result에 넣어주기
            result.insert(target_idx, target)
            print(result)
        else:
            break
        
    return result


d = [2, 4, 5, 1, 3]
print(insert_sort(d))