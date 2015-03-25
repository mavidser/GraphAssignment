def tarjan(g):
    index = {}
    S = []

    lowlink = {}
    onStack = {}

    result = []

    def strongconnect(v):
        index[v] = len(index)
        lowlink[v] = index[v]
        S.append(v)
        onStack[v]=True
        for w in g.get(v,[]):
            if w not in index:
                strongconnect(w)
                lowlink[v] = min(lowlink[w], lowlink[v])
            elif w in onStack and onStack[w]==True:
                lowlink[v] = min(lowlink[v], index[w])
        if lowlink[v] == index[v]:
            scc = []
            w = None
            while v != w:
                w = S.pop()
                scc.append(w)
                onStack[w]=False
            result.append(scc)

    for v in g:
        if not v in index:
            strongconnect(v)
    return result

graph = {}
for line in open('input.txt'):
  edge = line.strip().split()
  if edge[0] in graph:
    graph[edge[0]].append(edge[1])
  else:
    graph[edge[0]] = [edge[1]]

print tarjan(graph)
