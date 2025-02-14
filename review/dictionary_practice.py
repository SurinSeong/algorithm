# 딕셔너리를 사용해 학생 번호와 학생 이름이 대응된 학생 명부 만들기
student_info = {
    1 : '김민준',
    2 : '이유진',
    3 : '박승규'
}

# 학생번호 2번에 해당하는 학생 이름을 알고 싶다면
print(student_info[2])

# 새 학생을 학생 명부에 추가하려면 (4번 최재원)
student_info[4] = '최재원'
print(student_info)

# 학생 번호가 3번인 학생을 학생 명부에서 삭제하려면
del student_info[3]
print(student_info)