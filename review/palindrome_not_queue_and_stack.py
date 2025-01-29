def palindrome(string):
    # 문자열의 앞에서 비교할 위치
    front = 0
    # 문자열의 뒤에서 비교할 위치
    back = len(string)-1
    
    # 중간까지 검사하기
    while front < back:
        # 해당 위치에 있는 문자가 알파벳이 아니면 뒤로 이동
        if not string[front].isalpha():
            front += 1
        # 해당 위치에 있는 문자가 알파벳이 아니면 앞으로 이동
        elif not string[back].isalpha():
            back -= 1
        # 알파벳 문자가 있으면 두 문자 비교하고 다르면 회문이 아니다.
        elif string[front].lower() != string[back].lower():
            return False
        # 같으면 계속 비교하기 위해 숫자 변경
        else:
            front += 1
            back -= 1
    
    return True


print(palindrome('Wow'))
print(palindrome('Madam, I\'m Adam.'))
print(palindrome('Madam, I am Adam.'))