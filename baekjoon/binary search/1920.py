
def binary_search(arr: list, key: int):
    left = 0
    right = len(arr) - 1

    while True:
        center = (left + right) // 2
        if arr[center] == key:
            return 1
        elif arr[center] < key:
            left = center + 1
        else:
            right = center - 1

        if left > right:
            return 0


n = int(input())
A = [int(x) for x in input().split()]
m = int(input())
nums = [int(x) for x in input().split()]

A.sort()

for num in nums:
    print(binary_search(A, num))
