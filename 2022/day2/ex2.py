def main():

    # create dict with points
    points = {
        "X": 1,
        "Y": 2,
        "Z": 3
    }

    # get all possible combats
    options = {
        "A": {
            "X": "Z",
            "Y": "X",
            "Z": "Y"
        },
        "B": {
            "X": "X",
            "Y": "Y",
            "Z": "Z"
        },
        "C": {
            "X": "Y",
            "Y": "Z",
            "Z": "X"
        }
    }

    # initialize points counter
    counter = 0

    # open file
    with open("input.txt", "r") as file:
        # read each line
        for line in file:
            # retrieve what each player played
            play_other, instruction = line.rstrip().split(" ")

            # add points if you won or it is a draw (no adding for lose)
            if instruction == "Z": # win
                counter += 6
            elif instruction == "Y": # draw
                counter += 3

            # identify what you need to play
            play_you = options[play_other][instruction]

            # add points according to what you played
            counter += points[play_you]
    
    print("Total points: " + str(counter))



if __name__ == "__main__":
    main()