# 문자열 뒤집기
# 문자열 길이 // 2 : 교환 횟수
txt = list(input())
N = len(txt)

for i in range(N//2):
    txt[i], txt[N-1-i] = txt[N-1-i], txt[i]

print(txt)
print(txt[::-1])

txt_list = list(txt)

txt.reverse()

print(txt)