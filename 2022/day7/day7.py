import re

with open("input.txt", "r") as file:
    data = file.read().rstrip()
    data = data.split("\n")

    # initialize path
    path = ""
    # initialize dict with subdirs
    subdirs = {}
    # init dict with size of files in each folder
    sizes = {}
    # init total size
    total_size = 0

    # fill the dicts
    for line in data:
        # split elements from the line
        results = re.match(r"(?:(^\$) (cd |ls))?([^ ]*) ?(.*)?", line)
        commandline, commandtype, text1, text2 = results.groups()

        #  if line starts with $: command line
        if commandline != None:
            # if line starts with $ cd: move
            if commandtype.rstrip() == "cd":
                # move to the folder
                if text1 == "..":
                    # update path to go to the parent
                    path = "/".join(path.split("/")[:-1])
                    
                else:
                    # update position in the tree and retrieve the name of the current dir just entered
                    if path == "/" or path == "":
                        path += text1
                    else:
                        path += "/" + text1
                    
                    subdirs[path] = []
                    sizes[path] = 0
        # else: result
        else:
            # if line starts with dir
            if text1 == "dir":
                # add the dir to the tree and update parents dict
                if path == "/":
                    subdirs[path].append(path + text2)
                else:
                    subdirs[path].append(path + "/" + text2)
            # else: file name
            else:
                sizes[path] += int(text1)
                total_size += int(text1)

# calculate file's sizes

# recursive function to calcultae size of dir and its subdirs
def calculate_size(dir):
    # initialize sum with size of files in the dir (without subdir)
    sum = sizes[dir]
    # add subdirs
    for subdir in subdirs[dir]:
        if subdir in subdirs.keys():
            sum += calculate_size(subdir)
    return sum

# calculate space to delete to do the update
space_to_delete = total_size - (70000000 - 30000000)
delete = 0

# count size of each dir and sum
total = 0
for dir in subdirs:
    s = calculate_size(dir)
    if s < 100000:
        total += s
    if s > space_to_delete:
        if delete == 0:
            delete = s
        elif s < delete :
            delete = s

print("Solution 1: " + str(total))
print("Solution 2: " + str(delete))
