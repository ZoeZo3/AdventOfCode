def main():

    # create dict with points
    points = {
        "X": 1,
        "Y": 2,
        "Z": 3
    }

    # get all possible combats
    loose_options = ["AZ", "BX", "CY"]
    win_options = ["AY", "BZ", "CX"]
    draw_options = ["AX", "BY", "CZ"]

    # initialize points counter
    counter = 0

    # open file
    with open("input.txt", "r") as file:
        # read each line
        for line in file:
            # retrieve what each player played
            play_other, play_you = line.rstrip().split(" ")

            # add points if you won or it is a draw
            if play_other + play_you in win_options:
                counter += 6
            elif play_other + play_you in draw_options:
                counter += 3

            # add points according to what you played
            counter += points[play_you]
    
    print("Total points: " + str(counter))

            

if __name__ == "__main__":
    main()