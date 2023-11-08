with open("input.txt", "r") as file:
    data = file.readlines()

    # init counter for correct ordered pairs
    counter = 0


    i = 0
    while i < len(data):
        first = data[i]
        last = data[i + 1]
        # compare lines i and i + 1
        # if both are integers
        if first[1].isnumeric() and last[1].isnumeric():
            # if left < right then OK
            if int(first[1]) < int(last[1]):
                counter += i / 3
                break
        if first[1].isnumeric() and last[1].isnumeric() == False:
            

       
        i += 3
