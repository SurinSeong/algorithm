# 여섯자리 숫자 리스트에 저장하기
# 여섯자리 숫자 받기
num = int(input())

# 각 자리 수를 받을 리스트 만들기
count = [0] * 12 # 왜 12..? : baby-gin 문제 풀이 시, 구간에 따른 조사 방법을 통일하기 위해.

for i in range(6):
    count[num % 10] += 1
    num //= 10