with open("input.txt", "r") as file:
    data = file.read().split("\n\n")
    # for part 2
    common_div = 1

    # create dict with monkey's properties
    monkeys_dict = {}
    for monkey in data:
        params = monkey.split("\n")
        monkeys_dict[int(params[0][7])] = {
            "items": [int(i) for i in params[1].lstrip(" ").replace(",", "").split(" ")[2:]],
            "operation": params[2].split(" ")[-2:],
            "test": int(params[3].split(" ")[-1]),
            "true": int(params[4].split(" ")[-1]),
            "false": int(params[5].split(" ")[-1]),
            "items_checked": 0
        }
        common_div *= int(params[3].split(" ")[-1])
        
for i in range(10000):
    for m in range(len(monkeys_dict.keys())):
        monkey = monkeys_dict[m]
        for item in (monkey["items"]):
            # add it to the items_checked parameter
            monkey["items_checked"] += 1

            # operation on the worry level
            try:
                item = item * int(monkey["operation"][1]) if monkey["operation"][0] == "*" else item + int(monkey["operation"][1])
            except ValueError:
                item = item * item if monkey["operation"][0] == "*" else item + item

            # divide worry level for part 1
            #item = int(item / 3)

            #divide worry level for part 2
            item = item % common_div

            # test and throw item to following monkey
            if item % monkey["test"]:
                monkeys_dict[monkey["false"]]["items"].append(item)
            else:
                monkeys_dict[monkey["true"]]["items"].append(item)
        
        # remove items from current monkey
        monkey["items"] = []
    
# get ordered list of all the numbers of items checked
checked = [monkeys_dict[m]["items_checked"] for m in monkeys_dict]
checked.sort()

# calculate the monkey business
monkey_business = checked[-2] * checked[-1]

print("Answer is " + str(monkey_business))
