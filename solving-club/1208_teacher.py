# dump : 상자를 옮길 수 있는 횟수
dump = int(input())
# 상자들의 높이
box_heights = list(map(int, input().split()))

# dump 횟수만큼 반복
# 이번 덤프 때, 가장 높은, 낮은 상자의 높이 구하기
# 높낮이를 바꿔준다. => 인덱스를 알아야 함.
# 내장 함수 사용하기 => .index() (하지만, O(n)) / arr[idx] : O(1)
#  => sort() / 힙, 큐
# 내장 함수 사용하지 않으면 => 인덱스로 max, min을 구한다.
# 평탄화 완료 후, 최대 최소 상자 인덱스를 다시 구해야 한다.
# 주의! 덤프 횟수를 다 사용하지 않고 평탄화를 완료했을 경우도 생각해야 한다.
