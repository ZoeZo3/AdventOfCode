with open("input.txt", "r") as file:
    # read data
    data = file.read().rstrip()

    if len(data) > 3:  
        # create empty lists for the possible markers
        list_packet = []
        list_message = []

        i = 3
        ii = 13
        while i < len(data):
            if len(list_packet) < 1:
                # create list with first 4 elements
                list_packet = [data[0], data[1], data[2], data[3]]
            else:
                # update the list by removing first element and adding the next one
                list_packet = list_packet[1:4]
                list_packet.append(data[i])

            # check if the 4 caracter's list is a market: check if all 4 caracters are different
            if len(list_packet) == len(set(list_packet)):
                print("Number of caracters before first packet marker: " + str(i + 1))
                break
            
            # increment i
            i += 1

        while ii < len(data):
            if len(list_message) < 1:
                # create list with first 14 elements
                for j in range(0, ii + 1):
                    list_message.append(data[i])
            else:
                # update the list by removing first element and adding the next one
                list_message = list_message[1:14]
                list_message.append(data[ii])

            # check if the 4 caracter's list is a market: check if all 4 caracters are different
            if len(list_message) == len(set(list_message)):
                print("Number of caracters before first message marker: " + str(ii + 1))
                break
            
            # increment ii
            ii += 1

            

            