def main():

    # initialize max cal
    maximum_calories = 0

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
                # check if the previous one had the most calories 
                if current_elf_cal > maximum_calories:
                    maximum_calories = current_elf_cal
                # initialize var current_elf_cal for the new elf
                current_elf_cal = 0
    
    # print answer
    print(maximum_calories)

main()


