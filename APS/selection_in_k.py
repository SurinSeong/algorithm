# k 번째로 작은 원소 찾기
def select_k(a, k):
    for i in range(k):
        min_idx = i
        for j in range(i+1, len(a)):
            if a[min_idx] > a[j]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]

    return a[k-1]


arr = [10, 25, 64, 22, 11]

print(select_k(arr, 4))
