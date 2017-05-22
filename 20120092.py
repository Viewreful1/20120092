import sys
input = sys.stdin.readline

def DFS(src):
    print(src, end=' ')
    visited[src] = True
    for dest in adj[src]:
        if visited[dest] == False:
            DFS(dest)

def BFS(src):
    Q = [src]
    visited[src] = True
    while len(Q) > 0:
        src = Q.pop()
        print(src, end=' ')
        for dest in adj[src]:
            if visited[dest] == False:
                Q.insert(0,dest)
                visited[dest] = True

N,M,src = [int(x) for x in input().split()]
adj={}
V = []
for __ in range(M):
    u,v = [int(x) for x in input().split()]
    if u not in V:
        V.append(u)
        adj[u] = []
    if v not in V:
        V.append(v)
        adj[v] = []
    adj[u].append(v)
    adj[v].append(u)
V.sort()
for v in V:
    adj[v].sort()

visited={}
for v in V:
    visited[v] = False
DFS(src)
print()
visited={}
for v in V:
    visited[v] = False
BFS(src)
