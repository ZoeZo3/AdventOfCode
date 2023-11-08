# initialize counter for range included in another
counter1 = 0
# initialize counter for overlapping ranges
counter2 = 0

# read file
with open("input.txt", "r") as file:
    for pair in file:
        # get each number for each elf from each pair
        elf1_min, elf1_max = pair.split(",")[0].split("-")
        elf2_min, elf2_max = pair.split(",")[1].split("-")

        # transform str to int
        elf1_min, elf1_max, elf2_min, elf2_max = int(elf1_min), int(elf1_max), int(elf2_min), int(elf2_max)

        # check if one is contained in the other
        # case 1: elf 2 is contained in elf 1 // case 2: elf 1 is contained in elf 2
        if (elf1_min <= elf2_min and elf1_max >= elf2_max) or (elf2_min <= elf1_min and elf2_max >= elf1_max):
            counter1 += 1
        
        # check if ranges overlap
        if (elf1_min <= elf2_max and elf2_min <= elf1_max) or(elf2_min <= elf1_max and elf1_min <= elf2_max):
            counter2 += 1

print("Number of assignment pairs where one range fully contain the other: " + str(counter1))
print("Number of overlaping ranges: " + str(counter2))