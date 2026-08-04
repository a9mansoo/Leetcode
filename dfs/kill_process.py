from typing import List

class Solution:

    def killTree(self, curr_process, process_parent, result):
        process_children = process_parent.get(curr_process)
        if not process_children:
            return
        for child in process_children:
            result.append(child)
            self.killTree(child, process_parent, result)
        return result


    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        process_parent = {}

        for i in range(len(pid)):
            parent_process = ppid[i]
            if parent_process not in process_parent:
                process_parent[parent_process] = [pid[i]]
            else:
                process_parent[parent_process].append(pid[i])
        
        print(process_parent)
        if kill not in process_parent:
            return [kill]
        kill_list = [kill]
        return self.killTree(kill, process_parent, kill_list)
