import numpy as np

with open("input.txt", "r") as file:
    data = file.read().split("\n")
    # create a 2D array with the map
    map = np.array([[j for j in i] for i in data])

    # get coordinates of S and E and a's
    # for part 1
    #ls_all, cs_all = np.where(map == "S")
    # for part 2
    coords_mult = np.where((map == "S") | (map == "a"))
    ls_all = coords_mult[0]
    cs_all = coords_mult[1]
    le, ce = np.where(map == "E")
    le, ce = le[0], ce[0]

    # replace S and E with their value
    map[np.where(map == "S")] = "a"
    map[le, ce] = "z"
    
    # directions for each step
    directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

    # init var for the min distance with the number of elements in the array
    min_distance = map.size

    # for each starting point
    for i in range(len(ls_all)):
        # get coords for this starting point
        ls = ls_all[i]
        cs = cs_all[i]
        # init path        
        queue = [list([ls, cs])]
        distances = {(ls, cs): 0}

        # stop when blocked or arrived to destination
        while queue:
            ls, cs = queue.pop(0) # current position
            # check which directions are possible
            for d in directions:
                new_ls = ls + d[0]
                new_cs = cs + d[1]
                if 0 <= new_ls < len(map) and 0 <= new_cs < len(map[0]):
                    if ord(map[new_ls, new_cs][0]) - ord(map[ls, cs][0]) <= 1 and (new_ls, new_cs) not in distances:
                        distances[new_ls, new_cs] = distances[ls, cs] + 1
                        queue.append([new_ls, new_cs])
       
        try:
            if distances[(le, ce)] < min_distance:
                min_distance = distances[(le, ce)]
        except KeyError:
            pass
                    
    print("Min distance: " + str(min_distance))