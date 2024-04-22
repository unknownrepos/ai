Graph={
    1:[2,3],
    2:[3],
    3:[4],
    4:[1],
    5:[],
    6:[5]
}
visited=[]
queue=[]

def bfs(visited,Graph,node):
    visited.append(node)
    queue.append(node)
    while queue:
        s=queue.pop(0)
        print(s,end=" ")
        for neighbour in Graph[s]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

bfs(visited,Graph,1)
