# 단순하게 순열 생성하기
for a in range(1, 4):
    for b in range(1, 4):
        if a != b:
            for c in range(1, 4):
                if (c != a) and (c != b):
                    print(a, b, c)