# 가짜 동전 찾기 알고리즘

1. 하나씩 비교하기 (순차 탐색)

2. 반씩 그룹으로 나누어 비교하기 (이분 탐색)

- 알고리즘 효율성을 **저울질 횟수** 를 기준으로 생각해보기  
1번 방법은 일일이 비교하는 방법이기 때문에 계산 복잡도가 **O(n)** 이다.  
2번 방법은 절반씩 나누며 후보를 좁히는 방법이기 때문에 계산 복잡도가 **O(logN)** 이다.

=> 리스트 탐색 문제와 구조가 비슷한 문제

---

# 최대 수익 알고리즘

- 어떤 주식에 대해 특정 기간 동안의 가격 변화가 주어졌을 때, 그 한 주를 한 번 사고팔아 얻을 수 있는 최대 수익 계산 알고리즘
    - 손해가 나면 주식을 사고팔지 않아도 된다.  
        => 최대 수익은 항상 0 이상
    - 날짜별 주식 가격 정보가 주어진다.

## 문제 분석과 모델링

- 주식 거래로 수익을 내는 가장 좋은 방법  
    = 가장 쌀 때 사서 가장 비쌀 때 파는 것
- 최대 수익만 물어보았기 때문에 정확한 날짜 정보는 필요 없다.  
    => 정보를 단순화해서 각 날의 주식 가격만 뽑아 리스트로 만들어 사용한다.

## 방법 1. 가능한 모든 경우 비교하기

- 동명이인 찾는 문제에서 가능한 모든 사람을 비교하던 방식과 동일하다.
    - 사는 날을 중심으로 생각
- 계산 복잡도 : O(n^2)

## 방법 2. 한 번 반복으로 최대 수익 찾기

- 파는 날을 중심으로 생각
    - 파는 날 기준, 이전 날들의 주가 중 최솟값만 알면 최대 수익을 쉽게 계산
- 계산 복잡도 : O(n)

※ 방법 1(slow_way)과 방법 2(fast_way)의 걸리는 시간 차이 구하기

- 입력 크기를 100으로 입력했을 때는 fast와 slow의 계산 시간 차이가 40배 정도 난다.
- 입력 크기를 10000, 100000으로 입력했더니 차이가 3700배와 42000배로 급격히 벌어진다는 것을 알 수 있음.

---
