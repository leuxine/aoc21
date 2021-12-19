

def star1():
    grid = []
    with open('input.in', 'r') as file:
        for line in file:
            tmp = []
            for c in line.strip('\n'):
                tmp.append(int(c))
            grid.append(tmp)

    #for i in range(len(grid)):
    #    for j in range(len(grid)):
    #        print(grid[i][j], "", end="")
    #    print()
    #print()

    dp = [[0 for j in range(len(grid))] for i in range(len(grid))]

    for i in range(len(dp)):
        for j in range(len(dp)):
            if i == 0 and j == 0:
                dp[i][j] = grid[i][j]
            elif i == 0:
                dp[i][j] = dp[i][j-1] + grid[i][j]
            elif j == 0:
                dp[i][j] = dp[i-1][j] + grid[i][j]
            else:
                dp[i][j] = min(dp[i][j-1], dp[i-1][j]) + grid[i][j]


    #for i in range(len(dp)):
    #    for j in range(len(dp)):
    #        print(dp[i][j], "", end="")
    #    print()
    
    print(dp[len(grid)-1][len(grid)-1] - grid[len(grid)-1][len(grid)-1])

def star2():
    grid = []
    with open('small.in', 'r') as file:
        for line in file:
            tmp = []
            for c in line.strip('\n'):
                tmp.append(int(c))
            grid.append(tmp)

    #for row in grid:
    #    for el in row:
    #        print(el, "", end="")
    #    print()
    #print()

    l = len(grid)

    for i in range(l):
        for j in range(l, 5 * l):
            tmp = grid[i][j%l] + j // l
            if tmp > 9:
                grid[i].append(tmp % 10 + 1)
            else:
                grid[i].append(tmp)

    #for row in grid:
    #    for el in row:
    #        print(el, "", end="")
    #    print()
    #print()
    

    w = len(grid[0])

    for j in range(w):
        for i in range(l, 5 * l):
            num = grid[i%l][j%l] + i // l + j // l
            
            if j == 0:
                grid.append([])
            
            if num > 9:
                grid[i].append(num % 10 + 1)
            else:
                grid[i].append(num)

    #for row in grid:
    #    for el in row:
    #        print(el, "", end="")
    #    print()
    #print()

    dp = [[0 for j in range(len(grid))] for i in range(len(grid))]

    for i in range(len(dp)):
        for j in range(len(dp)):
            if i == 0 and j == 0:
                dp[i][j] = grid[i][j]
            elif i == 0:
                dp[i][j] = dp[i][j-1] + grid[i][j]
            elif j == 0:
                dp[i][j] = dp[i-1][j] + grid[i][j]
            else:
                dp[i][j] = min(dp[i][j-1], dp[i-1][j]) + grid[i][j]


    print(dp[len(grid)-1][len(grid)-1] - grid[0][0])

    #answer is between 2836 and 2829


star1()
star2()
