def main():
    
    # initialize priorities sum
    priorities = 0

    # open the input file
    with open("input.txt", "r") as file:
        # read each line
        for rucksack in file:
            # remove ending space and \n
            rucksack = rucksack.rstrip()
            # get the nb of items in each compartment of the bagpack
            len_compartment = int(len(rucksack) / 2)
            # get the lists of items in each compartment
            part1, part2 = [rucksack[0:len_compartment], rucksack[len_compartment: 2 * len_compartment]]

            # get the common item between the two lists
            common_item = find_common_item(part1, part2)

            # add it to the priorities sum
            priorities += convert_priority(common_item)

    # print result
    print("Sum of priorities: " + str(priorities))

def find_common_item(list1, list2):
    # find the first occurence of the common element between the 2 lists
    for i1 in list1:
        for i2 in list2:
            if i1 == i2:
                return i1

def convert_priority(item):
    # associate a number from 1 to 26 for each lower case letter
    if item.islower():
        return ord(item) - 96
    # associate a number from 27 to 52 for each upper case letter
    elif item.isupper():
        return ord(item) - 64 + 26
    # associate 0 to any other caracter
    else:
        return 0

main()