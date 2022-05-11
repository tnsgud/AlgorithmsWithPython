
n, m = map(int, input().split())
trees = [int(x) for x in input().split()]

left, right = 1, max(trees)

while left <= right:
    center = (left + right) // 2
    height = 0

    for h in trees:
        if h > center:
            height += h - center

    if height >= m:
        left = center + 1
    else:
        right = center - 1

print(right)
