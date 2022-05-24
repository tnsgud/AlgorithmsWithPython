
n = input()
cards = map(int, input().split())
m = input()
nums = map(int, input().split())

count = {}

for card in cards:
    if card in count:
        count[card] += 1
    else:
        count[card] = 1

for target in nums:
    num = count.get(target)

    if num is None:
        print(0, end=' ')
    else:
        print(num, end=' ')
