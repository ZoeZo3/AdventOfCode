import re
import copy

# init lists for the 2 parts from input file
part = 1
part1 = []
part2 = []

# init dict with the cranes strucutre
cranes = {}

# read the input file and get the 2 parts of the input
with open("input.txt", "r") as file:
    cranes_structure, moves = file.read().split("\n\n")
    cranes_structure = cranes_structure.split("\n")
    moves = moves.split("\n")

# fill the cranes dict to get the crane's structure
# read bakcwards
i = 0
for line in reversed(cranes_structure):
    # counter for the j-eme caracter
    j = 0
    # counter for the k-eme crane
    k = 1
    while j < len(line):
        # if last line
        if i == 0:
            caracter = line[j:j+3].strip(" ")
            cranes[caracter] = []
        else:
            caracter = re.sub(r"   |\[|\] |\]", "", line[j:j+3]).rstrip("\n")
            if caracter != "":
                cranes[str(k)].append(caracter)
        j += 4
        k += 1
    i += 1

# create a deep copy of the cranes dict for the second ex
cranes2 = copy.deepcopy(cranes)

# make the moves
for move in moves:
    # get each number from the move
    _, number_of_cranes, _, start, _, end = move.split(" ")

    # make the move for ex1
    for crane in range(int(number_of_cranes)):
        # add crane on top of end pile        
        cranes[end].append(cranes[start][- 1])        
        # remove last crane from start pile
        cranes[start] = cranes[start][:- 1]

    # make the move for ex2
    # add cranes on top of end pile
    cranes2[end] += cranes2[start][- int(number_of_cranes):]
    # remove cranes from start pile
    cranes2[start] = cranes2[start][:- int(number_of_cranes)]


# get the top cranes of each column
result1 = ""
result2 = ""
for col in cranes:
    result1 += cranes[col][len(cranes[col]) - 1]
for col in cranes2:
    result2 += cranes2[col][len(cranes2[col]) - 1]

print("The top cranes for question 1 are: " + result1)
print("The top cranes for question 2 are: " + result2)