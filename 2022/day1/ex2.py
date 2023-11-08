def main():

    # initialize max cal
    three_maximum_calories = [0, 0, 0]

    # read the file
    with open('entry.txt','r') as file:
        # initialize current elf's calories
        current_elf_cal = 0
        for line in file:
            # while same elf, add calories
            if line != "\n":
                current_elf_cal += int(line)
            # when new elf
            else:
                # check if the previous one had on of the 3 the most calories
                for m in three_maximum_calories:
                    if current_elf_cal > m:
                        three_maximum_calories.remove(m)
                        three_maximum_calories.append(current_elf_cal)
                        three_maximum_calories.sort()
                        break
                
                # initialize var current_elf_cal for the new elf
                current_elf_cal = 0
    
    # print answer
    print(sum(three_maximum_calories))

def sum(list):
    total = 0
    for l in list:
        total += l
    return total

main()
