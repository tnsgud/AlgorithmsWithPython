
k, n = map(int, input().split())

arr = []

for i in range(k):
    arr.append(int(input()))

left, right = 1, max(arr)

while left <= right:
    center = (left + right) // 2
    cnt = 0
    for a in arr:
        cnt += a // center

    if cnt < n:
        right = center - 1
    else:
        left = center + 1

print(right)
