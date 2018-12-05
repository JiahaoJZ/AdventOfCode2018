import re
list = [] #This will storage the input correctly
regex = re.compile(r'[\@\,\:x\#\n ]')
with open("day3input.txt") as r:
    for line in r:
        #Separate the input in numbers
        a = re.split(regex, line)
        #Cast to int the numbers and remove the empty ones
        a = [int(elem) for elem in a if elem]
        #Add to the list
        list.append(a)
        #In a is storaged a vector of 5 elements [id, shiftLeft, shiftTop, width, height]
    shiftLeft = max([a[1]+a[3] for a in list])
    shiftTop = max([a[2]+a[4] for a in list])
    #Create a grid that can fill all data
    grid = [[0 for i in range(0,shiftTop)] for j in range(0,shiftLeft)]

    Part2list = [l[0] for l in list] #This is for the part two to check what ID doesnt overlap

    #Fill the grid with the ID or -1 if collision detected
    for elem in list:
        width = elem[1] + elem[3]
        height = elem[2] + elem[4]
        for i in range(elem[1], width):
            for j in range(elem[2], height):
                if(grid[i][j] != 0): #collision
                    #These checks are for the part 2
                    if grid[i][j] in Part2list: #Remove the one who was on the table
                        Part2list.remove(grid[i][j])
                    if elem[0] in Part2list: #Remove the one who collides
                        Part2list.remove(elem[0])
                    #Each collision is represented by -1
                    grid[i][j] = -1
                else:
                    grid[i][j] = elem[0]

    ansPart1 = sum(a.count(-1) for a in grid)
    print("Parte1: " + str(ansPart1))
    print("Parte2: " + str(Part2list))
