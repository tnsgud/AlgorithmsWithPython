n, m, v = map(int, input().split())

node_map = [[] for i in range(n + 1)]
dfs_visible = []
bfs_visible = []

for i in range(m):
    n1, n2 = map(int, input().split())
    node_map[n1].append(n2)
    node_map[n2].append(n1)

for i in node_map:
    i.sort()


# dfs
def dfs(root: int):
    dfs_visible.append(root)

    for num in node_map[root]:
        if num not in dfs_visible:
            dfs(num)


def bfs(root: int):
    que = [root]
    bfs_visible.append(root)

    while que:
        num = que.pop(0)

        for node in node_map[num]:
            if node not in bfs_visible:
                bfs_visible.append(node)
                que.append(node)


dfs(v)
bfs(v)

print(' '.join(map(str, dfs_visible)))
print(' '.join(map(str, bfs_visible)))
