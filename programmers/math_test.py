"""
[모의고사]
- 1번 수포자 : 12345 돌아가면서
- 2번 수포자 : 21232425 순으로
- 3번 수포자 : 3311224455 순으로

- 1번부터 마지막 문제까지 정답이 배열로 주어진다.
- 가장 많은 문제를 맞힌 사람은?

[조건]
- 시험 최대 10,000문제
- 가장 높은 점수를 받은 사람이 여럿이면 오름차순 정렬
"""
def find_highest(answers, f, s, t):
    # 1, 2, 3번의 총 점수
    scores = [0]*3
    
    for i, answer in enumerate(answers):
        # 비교 하기 위해 인덱스를 맞췄다.
        fi, si, ti = i % len(f), i % len(s), i % len(t)
        
        # 정답과 제출한 답이 맞으면 + 1
        if answer == f[fi]:
            scores[0] += 1
        
        if answer == s[si]:
            scores[1] += 1
            
        if answer == t[ti]:
            scores[2] += 1
    
    return scores    
    

def solution(answers):
    N = len(answers)
    first = [1, 2, 3, 4, 5]
    second = [2, 1, 2, 3, 2, 4, 2, 5]
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    # 점수들 확인하기
    scores = find_highest(answers, first, second, third)
    
    # 가장 높은 점수
    max_s = max(scores)
    
    answer = []
    
    for i, score in enumerate(scores, 1):
        if max_s == score:
            answer.append(i)

    return answer


answers = [1, 3, 2, 4, 2]
print(solution(answers))