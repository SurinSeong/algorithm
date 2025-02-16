# 버블 정렬 과정
"""
55 7 78 12 42
"""

def bubble_sort(arr, n):
    for i in range(n-1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


# 카운팅 정렬
"""
0 4 1 3 1 2 4 1
"""

def counting_sort(arr, n):
    max_num = max(arr)
    counts = [0] * (max_num+1)
    
    for num in arr:
        counts[num] += 1
        
    # counts 누적합
    for i in range(1, max_num+1):
        counts[i] += counts[i-1]
        
    # 새로 배열할 빈 리스트를 만든다.
    temp = [0] * n
    
    for j in range(n-1, -1, -1):
        counts[arr[j]] -= 1
        temp[counts[arr[j]]] = arr[j]
    
    return temp