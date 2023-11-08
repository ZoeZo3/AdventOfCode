with open("input.txt", "r") as file:
    data = file.read()
    grid = data.split("\n")
    height = len(grid)
    width = len(grid[0])
    total = 0
    score = 0

    for i in range(height):
        for j in range(width):
            # init variables
            is_hidden = 0
            view_u, view_d, view_l, view_r = 0, 0, 0, 0

            # check if tree is hidden from the top of the grid
            for up in range(i - 1, -1, -1): # decreasing increment to start from the trees closer to the current tree
                # increment view counter, with maximum of 3 (p2)
                view_u += 1
                # if other tree is bigger or equal, tree is hidden
                if grid[up][j] >= grid[i][j]:
                    is_hidden += 1
                    break
                
            # check if tree is hidden from the bottom of the grid
            for down in range(i + 1,height):
                # increment view counter, with maximum of 3 (p2)
                view_d += 1
                # if other tree is bigger or equal, tree is hidden
                if grid[down][j] >= grid[i][j]:
                    is_hidden += 1
                    break

            # check if tree is hidden from the left of the grid
            for l in range(j - 1, -1, -1): # decreasing increment to start from the trees closer to the current tree
                # increment view counter, with maximum of 3 (p2)
                view_l += 1
                # if other tree is bigger or equal, tree is hidden
                if grid[i][l] >= grid[i][j]:
                    is_hidden += 1
                    break

            # check if tree is hidden from the right of the grid
            for r in range(j + 1, width):
                # increment view counter, with maximum of 3 (p2)
                view_r += 1
                # if other tree is bigger or equal, tree is hidden
                if grid[i][r] >= grid[i][j]:
                    is_hidden += 1
                    break
            
            # if tree is not hidden from all directions, it is visible
            if is_hidden < 4:
                total += 1
            
            # scenic score
            score = max(view_u * view_d * view_l * view_r, score)

print("Answer 1: " + str(total))
print("Answer 2: " + str(score))