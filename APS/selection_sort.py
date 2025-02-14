# 선택 정렬 구현하기
def selection_sort(data):
    for i in range(len(data)-1):
        min_idx = i
        for j in range(i+1, len(data)):
            # 최솟값보다 더 작은 값이 나왔다면
            if data[min_idx] > data[j]:
                min_idx = j
        data[i], data[min_idx] = data[min_idx], data[i]
    return data


arr = [10, 25, 64, 22, 11]

print(selection_sort(arr))