input = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"

filesystem = input.split('\n')
print(filesystem)

stack = []

def calculate_depth(file_dir):
    depth = file_dir.count('\t')
    return depth

def clean_filename(file):
    return file.replace('\t', '')

max_depth = max([calculate_depth(file_dir) for file_dir in filesystem])
max_absolute_path = -1

curr_depth = 1

for file in filesystem:
    depth = calculate_depth(file)
    filename = clean_filename(file)

    while stack and len(stack) > depth:
        stack.pop()

    if stack:
        curr_name = stack[-1] + "/" + filename
    else:
        curr_name = filename
    
    if "." in curr_name:
        max_absolute_path = max(max_absolute_path, len(curr_name))
    stack.append(curr_name)
