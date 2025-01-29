# 학생 번호로 학생 이름을 찾는 문제
# 학생 번호와 이름이 주어졌을 때,
# 학생 번호를 입력하면 그 학생 번호에 해당하는 이름을 돌려준다.

def find_student_name(student_info, find_no):
    '''
    학생 번호로 학생 이름 찾기
    - 학생 번호를 입력하면, 그 학생 번호에 해당하는 이름을 돌려준다.
    - 해당 학생 번호가 없다면 물음표 반환
    '''
    if find_no in student_info:
        return student_info[find_no]
    else:
        return '?'


sample_info = {
    39 : 'Justin',
    14 : 'John',
    67 : 'Mike',
    105 : 'Summer'
}

print(find_student_name(sample_info, 14))
print(find_student_name(sample_info, 90))