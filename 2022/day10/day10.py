with open("input.txt", "r") as file:
    data = file.readlines()

    # init variables
    cycle = 1
    X = 1
    strength = 0
    CTR = [["." for i in range(40)] for j in range(6)]
    
    for line in data:
        #print(line.rstrip("\n"))
        # get the action and number values
        action, *value = line.rstrip("\n").split(" ")

        action_cycles = 2 if action == "noop" else 1

        while action_cycles <= 2:  
            # check if cycle one of the threshold
            if (cycle - 20) % 40 == 0:
                strength += X * cycle

            # if second cycle of add action, update X
            if action_cycles == 2 and action == "addx":
                X += int(value[0])
            
            sprite = [X-1, X, X+1]
            i = int(cycle / 40)
            j = cycle % 40
            if j in sprite:
                CTR[i][j] = "#"
            
            # increment counters
            cycle += 1
            action_cycles += 1

print("Answer to question 1 is: " + str(strength))
# print result
for line in CTR:
    formatted_line = "".join(i for i in line)
    print(formatted_line)
