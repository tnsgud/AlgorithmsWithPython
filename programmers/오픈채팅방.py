
record = [x for x in input().split(',')]
user = {}
actions = []
answer = []

for re in record:
    data = re.split()
    action, user_id = data[0], data[1]

    if action in ("Enter", "Change"):
        user[user_id] = data[2]

    actions.append((action, user_id))

for actionData in actions:
    event, user_id = actionData

    if event == 'Enter':
        answer.append(f'{user[user_id]}님이 들어왔습니다.')
    elif event == 'Leave':
        answer.append(f'{user[user_id]}님이 나갔습니다.')


print(answer)
