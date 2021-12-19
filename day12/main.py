

def amt(node, path):
    count = 0
    for n in path:
        if n == node:
            count += 1
    return count

def dfs(curr, end, graph, path, star):
    path.append(curr)
    if curr == end:
        return 1
    else:
        count = 0
        for n in graph[curr]:
            if n.isupper() or n not in path:
                count += dfs(n, end, graph, path.copy(), star)
            elif star and n != 'start':
                count += dfs(n, end, graph, path.copy(), False)
        return count

def stars():
    graph = dict()
    with open('input.in', 'r') as file:
        for line in file:
            edge = line.strip('\n').split('-')
            graph.setdefault(edge[0], []).append(edge[1])
            graph.setdefault(edge[1], []).append(edge[0])

    print("the number of distinct paths is %d\n" % (dfs('start', 'end', graph, \
        [], False)))

    print("if we go to small caves twice the amount is %d\n" % (dfs('start', \
        'end', graph, [], True)))

stars()
