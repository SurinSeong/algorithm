"""
[가운데를 말해요]
- 백준이가 정수를 하나씩 외친다.
- 동생은 지금까지 백준이가 말한 수 중에서 '중간값'을 말해야 한다.
- 외친 수의 개수가 짝수 개라면 중간에 있는 두 수 중 작은 수 말하기

[조건]
- 1 <= N <= 100,000
- -10,000 <= 정수 <= 10,000
"""
"""
중간값 유지 규칙:

최대힙은 중간값보다 작은 값들을 저장하며, 최소힙은 중간값보다 큰 값들을 저장.
두 힙의 크기는 같거나, 최대힙의 크기가 하나 더 많아야 한다.

새로운 숫자가 들어올 때:

새로운 숫자가 들어오면, 먼저 어느 힙에 넣을지를 결정:
최대힙에 넣을 수 있는 경우, 그 숫자가 중간값보다 작다면 최대힙에 넣고, 나머지 숫자는 최소힙에 넣는다.
최소힙에 넣을 수 있는 경우, 그 숫자가 중간값보다 크다면 최소힙에 넣고, 나머지 숫자는 최대힙에 넣는다.
두 힙의 크기를 맞춘다. (최대힙의 크기가 최소힙보다 1개 많아야 한다)

중간값을 찾는 방법:

최대힙의 루트 값이 항상 중간값이 된다(홀수 개일 때).
두 힙의 크기가 같을 때는 두 힙의 루트 값들 중 평균을 구할 수 있다(짝수 개일 때).
"""
import heapq

class MedianFinder:
    def __init__(self):
        # 최대힙 (작은 절반), 최소힙 (큰 절반)
        self.max_heap = []  # 음수로 최대힙 구현
        self.min_heap = []

    def addNum(self, num: int) -> None:
        # max_heap에 먼저 넣고, 최소값을 min_heap로 이동
        if not self.max_heap or num <= -self.max_heap[0]:
            heapq.heappush(self.max_heap, -num)  # 최대힙에는 음수로 넣어줌
        else:
            heapq.heappush(self.min_heap, num)

        # 두 힙의 크기 균형 맞추기
        if len(self.max_heap) > len(self.min_heap) + 1:
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
        elif len(self.min_heap) > len(self.max_heap):
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))

    def findMedian(self) -> float:
        # 중간값 찾기
        if len(self.max_heap) > len(self.min_heap):
            return -self.max_heap[0]
        else:
            return (-self.max_heap[0] + self.min_heap[0]) / 2.0 

# 

    

# 백준이가 외치는 정수의 개수
N = int(input())

min_heap, max_heap = [], []

for i in range(N):

    integer = int(input())    # 현재 외치는 정수
    if mid_num < integer:    # 중간값보다 현재 정수가 크면
        # 최소힙
    
    
        
        
        
    

    
# 동생이 말해야 하는 중간값 찾기


"""
1 5 2 10 -99 7 5
"""
  