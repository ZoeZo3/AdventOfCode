with open("input.txt", "r") as file:
    data = file.readlines()

    # init variables
    x_list = []
    x = 1
    CTR = [["." for i in range(40)] for j in range(6)]
    
    for line in data:
        # get the action and number values
        action, *value = line.rstrip("\n").split(" ")
        if action == "addx":
            x_list.extend([x,x])
            x += int(value[0])   
        else:
            x_list.append(x)
    
    strength = sum(x_list[i-1] * i for i in range(20, len(x_list) + 1, 40))
    print("Answer to question 1 is: " + str(strength))

    for cycle in range(len(x_list)):
        x = x_list[cycle]
        sprite = [x-1, x, x+1]
        i = int(cycle / 40)
        j = cycle % 40
        if j in sprite:
            CTR[i][j] = "#"

    # print result
    for line in CTR:
        formatted_line = "".join(i for i in line)
        print(formatted_line)

