prerequisites = [[0,1], [0,2], [1,3], [1,4], [3,4]]
numCourses = 5

graph = {i: [] for i in range(numCourses)}

for prereq in prerequisites:
    node = prereq[0]
    edge = prereq[1]

    if node not in graph:
        graph[node] = [edge]
    else:
        graph[node].append(edge)


def canFinish(n, graph):
    visitedNodes = set()

    def dfs(node, graph):
        if node in visitedNodes:
            return False
        elif graph[node] == []:
            return True
        
        visitedNodes.add(node)
        for neigh in graph[node]:
            if not dfs(neigh, graph):
                return False
        visitedNodes.remove(node)
        graph[node] = []
        return True
    
    for n in range(numCourses):
        if not dfs(graph[n], graph):
            return False
    return True
