class FileSystem:

    def __init__(self):
        self.filesystem = {}
        

    def createPath(self, path: str, value: int) -> bool:
        if path in self.filesystem:
            return False
        split_path = path.split("/")
        curr_path = ""
        for new_path in split_path[:-1]:
            if new_path == "":
                continue
            curr_path += f"/{new_path}"
            if curr_path not in self.filesystem:
                return False
        self.filesystem[path] = value
        return True
        

    def get(self, path: str) -> int:
        return self.filesystem.get(path, -1)
        
ops = ["FileSystem","createPath","createPath","createPath","createPath","createPath","get"]
arguments = [[],["/a/b/c",1],["/a",1],["/a/b",2],["/a/b/c",3],["/a/b/c",5],["/a/b/c"]]

obj = None
for op, args in zip(ops, arguments):
    if op == "FileSystem":
        obj = FileSystem()
    elif getattr(obj, op):
        result = getattr(obj, op)(*args)