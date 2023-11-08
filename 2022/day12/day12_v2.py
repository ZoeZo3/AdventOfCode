import numpy as np

with open("input.txt", "r") as file:
    data = file.read().split("\n")
    # create a 2D array with the map
    map = np.array([[j for j in i] for i in data])

    # get coordinates of end point
    le, ce = np.where(map == "E")
    le, ce = le[0], ce[0]

    # get coordinates for start points
    # for part 1
    ls_all, cs_all = np.where(map == "S")
    # for part 2
    coords_mult = np.where((map == "S") | (map == "a"))
    #ls_all = coords_mult[0]
    #cs_all = coords_mult[1]

    # replace S and E with their value
    map[np.where(map == "S")] = "a"
    map[le, ce] = "z"
    
    # directions for each step
    directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

    # init var for the min distance with the number of elements in the array
    min_distance = map.size

    # start from the end point
    # init path        
    queue = [list([le, ce])]
    distances = {(le, ce): 0}

    # stop when blocked or arrived to destination
    while queue:
        l1, c1 = queue.pop(0) # current position
        # check which directions are possible
        for d in directions:
            l2 = l1 + d[0]
            c2 = c1 + d[1]
            if 0 <= l2 < len(map) and 0 <= c2 < len(map[0]):
                if ord(map[l1, c1][0]) - ord(map[l2, c2][0]) <= 1 and (l2, c2) not in distances:
                    distances[l2, c2] = distances[l1, c1] + 1
                    queue.append([l2, c2])
    
    # for part 2, get the min distance from all starting points and order it
    dist = [distances[l, c] for l, c in zip(coords_mult[0], coords_mult[1]) if (l, c) in distances]
    dist.sort()
                    
    print("Min distance question 1: " + str(distances[ls_all[0], cs_all[0]]))
    print("Min distance question 2: " + str(dist[0]))