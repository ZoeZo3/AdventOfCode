# init directions dict
directions = {
    "L": [-1, 0],
    "R": [1, 0],
    "U": [0, 1],
    "D": [0,-1]
}

# init head, tail and positions array for pb1
positions = [list([0,0])]

# init rope and positions array for pb2
positions2 = [list([0,0])]
    
def main():
    with open("input.txt", "r") as file:
        data = file.readlines()
    
    # move the short rope
    positions = make_moves(data, 2)

    # move the long rope
    positions2 = make_moves(data, 10)

    print("Solution 1: " + str(len(positions)))
    print("Solution 2: " + str(len(positions2)))

def make_moves(data, len_):
    # init the rope and positions lists
    rope = [[0,0] for i in range(len_)]
    positions = []

    for move in data:
        dir, times = move.rstrip("\n").split(" ")

        # move the rope "times" times
        for _ in range(int(times)):
            # move the short rope
            for knot in range(len(rope)):
                # move head
                if knot == 0:
                    rope[knot][0] += directions[dir][0]
                    rope[knot][1] += directions[dir][1]
                # move the rest of the rope
                else:
                    move_tail(rope[knot], rope[knot - 1], dir)
            
            # add it to the tail's distinct positions
            if rope[len_ - 1] not in positions:
                positions.append(list(rope[len_ - 1]))

    return positions
    

def move_tail(current, previous, dir):
    # move current if not touching previous
    if current[0] not in [previous[0]-1, previous[0], previous[0]+1] or current[1] not in [previous[1]-1, previous[1], previous[1]+1]:
        # if current and previous are in the same row or column, move in the dir 
        if current[0] == previous[0] or current[1] == previous[1]:
            current[0] += (previous[0]-current[0])/2
            current[1] += (previous[1]-current[1])/2
            
        # if H and T are not in the same row or column, move in diagonal
        else:
            current[0] += int((previous[0]-current[0])/abs(previous[0]-current[0]))
            current[1] += int((previous[1]-current[1])/abs(previous[1]-current[1]))

main()