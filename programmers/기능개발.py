
progresses = [int(x) for x in input().split()]
speeds = [int(x) for x in input().split()]
answer = []

while progresses:
    for i in range(len(progresses)):
        progresses[i] += speeds[i]

    cnt = 0
    while progresses and progresses[0] >= 100:
        progresses.pop(0)
        speeds.pop(0)
        cnt += 1

    if cnt > 0:
        answer.append(cnt)

print(answer)
