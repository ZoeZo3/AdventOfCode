import re

with open("input.txt", "r") as file:
    data = file.read().rstrip()
    data = data.split("\n")

    # initialize files tree
    tree = {"/": {}}
    # init position tree to follow where we are
    position = tree
    # initialize path list to follow the path
    path = []
    # initialize dict with subdirs
    subdirs = {}

    # fill the tree
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
                    path = path[:-1]
                    position = tree
                    for dir in path:
                        position = position[dir]
                else:
                    # update position in the tree and retrieve the name of the current dir just entered
                    position = position[text1]
                    path.append(text1)
                    subdirs["/".join(i for i in path)] = []
        # else: result
        else:
            # if line starts with dir
            if text1 == "dir":
                # add the dir to the tree and update parents dict
                if text2 not in position.keys():
                    position[text2] = {}
                    subdirs["/".join(i for i in path)].append(text2)
            # else: file name
            else:
                if "file" not in position.keys():
                    position["files"] = {}
                position["files"][text2] = text1

# calculate file's sizes

# init sum with files on the dir
def calculate_size(dir):
    # add sizes from files in the dir (without subdir)
    sum = 0
    files = a
    if "files" in dir.keys():
        for f in dir["files"].keys():
            sum += dir["files"][f]
    
    # add subdirs
    for subdir in  dir.keys():
        if subdir != "files":
            sum += calculate_size(subdir)
    
    return sum



print(subdirs)
