# 반씩 그룹으로 나누어 비교하기
'''
- 주어진 동전을 절반씩 두 그룹으로 나눠서 양팔 저울에 올렸을 때 한쪽이 가볍다면 그 가벼운 쪽에 가짜 동전이 존재한다.
'''


# 무게 비교 함수
def weigh(a, b, c, d):
    # 가짜 동전 번호
    fake = 29
    # a~b에 있다면
    if (a <= fake <= b):
        return -1
    # c~d에 있다면
    if (c <= fake <= d):
        return 1
    
    # 같다면
    return 0
    
    
# 가짜 동전 찾는 함수 ==> 계산 복잡도 : O(logN)
def find_fake_coin(left, right):
    # 종료 조건 설정 : 가짜 동전이 있을 범위 안에 동전이 한 개뿐이면, 그 동전이 가짜 동전이다.
    if left == right:
        return left
    
    # left와 right까지에 놓인 동전을 두 그룹으로 나눈다.
    # 동전의 수가 홀수이면 두 그룹으로 나누고 하나가 남는다.
    half = (right - left + 1) // 2
    group1_left = left
    group1_right = left + half - 1
    group2_left = left + half
    group2_right = group2_left + half - 1
    
    print(f'GROUP1 >> {group1_left} ~ {group1_right}\nGROUP2 >> {group2_left} ~ {group2_right}\n')
    
    # 나눠진 두 그룹을 weigh() 함수를 이용해 저울질하기
    result = weigh(group1_left, group1_right, group2_left, group2_right)
    # 그룹 1이 가벼우면
    if result == -1:
        return find_fake_coin(group1_left, group1_right)
    # 그룹 2이 가벼우면
    elif result == 1:
        return find_fake_coin(group2_left, group2_right)
    # 나뉜 두 그룹 안에 가짜 동전이 없다면
    else:
        return right
    

n = 100
print(find_fake_coin(0, n-1))