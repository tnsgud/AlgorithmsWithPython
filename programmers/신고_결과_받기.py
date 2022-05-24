
id_list = input().split()
report = set(input().split(','))
k = int(input())
answer = []
id_map = {}
repo_cnt_map = {}

for id in id_list:
    id_map[f'{id}'] = {'count': 0, 'from': [], 'repo': 0}

for repo in report:
    ids = repo.split()
    id_map[ids[1]]['count'] += 1
    id_map[ids[1]]['from'].append(ids[0])

for data in id_map.values():
    if data['count'] >= k:
        for id in data['from']:
            id_map[id]['repo'] += 1

for data in id_map.values():
    answer.append(data['repo'])

print(answer)
