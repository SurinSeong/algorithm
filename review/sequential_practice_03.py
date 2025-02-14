# 학생 번호와 이름이 리스트로 주어졌을 때때
# 학생 번호를 입력하면 학생 번호에 해당하는 이름을 순차 탐색으로 찾아 돌려주는 함수
# 해당하는 학생 번호가 없어면 물음표 반환
def search_student_name(name_list, number_list, target):
    for i in range(len(number_list)):
        if target == number_list[i]:
            return name_list[i]
    else:
        return '?'
    
    
sample_no = [39, 14, 67, 105]
sample_name = ['Justin', 'John', 'Mike', 'Summer']

print(search_student_name(sample_name, sample_no, 105))
print(search_student_name(sample_name, sample_no, 777))