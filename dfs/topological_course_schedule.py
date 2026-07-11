class Solution:

    def dfs(self, src, adj, path, visited):
        if src in path:
            return False
        
        if src in visited:
            return True
        
        visited.add(src)
        path.add(src)
        for neighbour in adj[src]:
            if not self.dfs(neighbour, adj, path, visited):
                return False
        
        path.remove(src)
        return True

    def canFinish(self, numCourses: int, prerequisites) -> bool:
        graph = {}
        for course in range(numCourses):
            graph[course] = []
        
        for prereq in prerequisites:
            prereq_course = prereq[0]
            course = prereq[1]
            graph[course].append(prereq_course)
        
        path = set()
        visited = set()
        for src in graph:
            if not self.dfs(src, graph, path, visited):
                return False
        return True

sol = Solution()
sol.canFinish(numCourses=3, prerequisites=[[1,0],[2,0],[0,2]])