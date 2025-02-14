# 회문 찾기
# 회문 : 순서대로 읽어도 거꾸로 읽어도 그 내용이 같은 낱말이나 문장
'''
문자열이 회문인지 아닌지를 판단하여 회문이면 True, 아니면 False 반환 알고리즘
- 낱말 사이에 있는 공백이나 문장 기호 등은 무시
- 큐와 스택에서 차례로 꺼낸 값이 모두 같으면 회문이다.
'''



def palindrome(s):
    '''
    회문 찾기 알고리즘
    입력 : s, 출력 : 회문이면 True, False
    '''
    # 큐와 스택을 리스트로 정의
    queue, stack = [], []
    
    # 1단계 : 문자열의 알파벳 문자를 각각 큐와 스택에 넣음
    for char in s:
        # 해당 문자가 알파벳이면 (공백, 특수문자, 숫자가 아니라면)
        if char.isalpha():
            # 큐와 스택에 각각 그 문자를 추가 (소문자로)
            queue.append(char.lower())
            stack.append(char.lower())
        
    # 2단계 : 큐와 스택에 들어 있는 문자를 꺼내면서 비교
    # 큐에 문자가 남아 있는 동안 반복
    while queue:
        # 큐와 스택에서 꺼낸 문자가 다르면 회문이 아님
        if queue.pop(0) != stack.pop():
            return False
    else:
        return True


print(palindrome('Wow'))
print(palindrome('Madam, I\'m Adam.'))
print(palindrome('Madam, I am Adam.'))