startGene = "AACCGGTT"
endGene = "AAACGGTA"
bank = set(["AACCGGTA","AACCGCTA","AAACGGTA"])


from collections import deque

map = {
    "A": ["T", "C", "G"],
    "T": ["A", "C", "G"],
    "C": ["A", "T", "G"],
    "G": ["A", "T", "C"]
}


def bfs():
    q = deque()

    visited = set()
    mutations = 0
    q.append(startGene)
    visited.add(startGene)

    while q:

        for _ in range(len(q)):
            curr_gene = q.popleft()

            if curr_gene == endGene:
                return mutations

            for i in range(len(curr_gene)):
                for char in "ACTG":
                    if char == curr_gene[i]:
                        continue
                    new_gene = curr_gene[:i] + char + curr_gene[i+1:]
                    if new_gene in bank and new_gene not in visited:
                        visited.add(new_gene)
                        q.append(new_gene)
        mutations += 1
    return -1


print(bfs())
