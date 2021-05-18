class DAG:
    def __init__(self, vertices):
        self.graph = {}
        self.numV = vertices
        for i in range(vertices):
            self.graph[i] = []

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def topologicalSortUtil(self, vertex, visited, stack):
        visited[vertex] = True

        for neighbour in self.graph[vertex]:
            if visited[neighbour] == False:
                self.topologicalSortUtil(neighbour, visited, stack)

        stack.append(vertex)

    def topologicalSort(self):
        stack = []
        visited = [False] * self.numV
        for i in range (self.numV):
            if visited[i] == False:
                self.topologicalSortUtil(i, visited, stack)
        print (stack[::-1])
 
    def show(self):
        return self.graph

##########################################################

def dfs(graph, vertex, path):
    path += [vertex]

    for neighbour in graph[vertex]:
        if neighbour not in path:
            path = dfs(graph, neighbour, path)

    return path

#########################################################

def bfs(graph, vertex):
    visited = []
    queue = []
    visited.append(vertex)
    queue.append(vertex)

    while queue:
        s = queue.pop(0)
        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
    
    return visited
