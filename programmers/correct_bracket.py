# 올바른 괄호
# '(' 로 열렸으면 반드시 ')'로 닫혀야 한다.

# 입출력 예시
# "()()", "(())()", ")()(", "(()("

'''
replace() 함수는 시간복잡도가 O(n^2)정도로 높기 때문에 시간 초과가 발생한다. (오래 걸림)
따라서, 알고리즘 분류를 활용해 stack 원리를 사용하면 시간복잡도가 낮아진다.
'''

# replace 함수 사용
def solution(s):
    answer = True

    while True:
        if '()' in s:
            s = s.replace('()', '')
        else:
            break
    
    if s != '':
        answer = False
    else:
        answer = True

    return answer


# stack 알고리즘 사용
def solution(s):
    stack = []
    target = '()'
    for i in range(len(s)):
        # 일단 stack에 괄호 넣어주기
        stack.append(s[i])

        if (s[i] == ')') and ''.join(stack[-len(target):]) == target:
            del stack[-len(target):]
    
    if stack:
        return False
    else:
        return True
        
# print()
print(solution(')()('))


