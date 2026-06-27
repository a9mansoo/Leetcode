clips = [[0,2],[4,6],[8,10],[1,9],[1,5],[5,9]]
time = 10
clips.sort()
print(clips)
curr_end = 0
n = len(clips)
last_extension = -1
count = 0
i = 0

while curr_end < time:

    while i < n and clips[i][0] <= curr_end:
        last_extension = max(last_extension, clips[i][1])
        i += 1
    
    if last_extension == curr_end:
        count = -1
        break
    
    curr_end = last_extension
    count += 1


print(count)
