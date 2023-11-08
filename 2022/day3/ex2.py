def main():
    
    # initialize priorities sum
    priorities = 0

    # open the input file
    with open("input.txt", "r") as file:
        # read all lines
        rucksacks = file.readlines()

        # browse lines 3 by 3
        for i in range(int(len(rucksacks) / 3)):
            r1, r2, r3 = [rucksacks[3*i].rstrip(), rucksacks[3*i + 1].rstrip(), rucksacks[3*i + 2].rstrip()]

            # get the common item between the two lists
            common_item = find_common_item(r1, r2, r3)

            # add it to the priorities sum
            priorities += convert_priority(common_item)

    # print result
    print("Sum of priorities: " + str(priorities))

def find_common_item(list1, list2, list3):
    # find the commo n element between the 3 lists
    for i1 in list1:
        for i2 in list2:
            if i1 == i2:
                for i3 in list3:
                    if i2 == i3:
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