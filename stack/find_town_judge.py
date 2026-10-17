n = 4
trust = [[1,3],[4,3],[2,3]]

def find_town_judge(trust):
        indegree = [0]*n
        outdegree = [0]*n

        for src, dest in trust:
            outdegree[src-1] += 1
            indegree[dest-1] += 1
        
        judge_candidate = None

        for i in range(len(indegree)):
            if indegree[i] == (n-1) and outdegree[i] == 0:
                judge_candidate = i
        
        return -1 if judge_candidate is None else judge_candidate + 1
