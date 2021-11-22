 
def BFS (A):

    queue = []

    marked = []
    distance = []

    for i in range(len(A)):
        new = []
        newD = []
        for j in i:
            new.append(0)
            newD.append(0)

        marked.append(new)
        distance.append(newD)

    distance = 0
    marked[0][0] = 1
    queue.append(A[0][0])

    while len(queue) != 0:

        v = queue[0]
        i = v[0]
        j = v[1]
        adjacents = [[i+1, j], [i, j+1]]
            
        for adj in adjacents:
            if marked[adj[0]][adj[1]] is 0:
                marked[adj[0]][adj[1]] = 1
                distance[adj[0]][adj[1]] = distance [i][j] + 1
                queue.append([adj[0], adj[1]])
                 
