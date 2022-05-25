
lottos = [int(x) for x in set(input().split())]
win_nums = [int(x) for x in input().split()]

if lottos.__contains__(0):
    lottos.remove(0)

answer = [7-(6-len(lottos)), 7]

for num in lottos:
    if num in win_nums:
        answer[0] -= 1
        answer[1] -= 1

for ans in answer:
    if ans == 7:
        answer[answer.index(ans)] = 6

print(answer)

