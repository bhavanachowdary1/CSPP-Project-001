def checkShip(grid, ship):
    count=0
    for i in ship:
        if grid[i[0]][i[1]]==1:
            count=count+1
            if count==len(ship):
                return True
        else:
            return False
grid = [ [1, 1, 2, 1], [1, 1, 2, 1], [1, 1, 2, 1], [2, 2, 2, 1] ]
numShips=2
print(checkShip(grid,ship))

# def addShips(grid, numShips):
#     while (numShips!=0):
#         ship=createShip()
#         if checkShip(grid, ship):
#             for i in ship:
#                 grid[i[0]][i[1]]=SHIP_UNCLICKED
#             numShips-=1
#     return grid
# print(addships(grid, numShips))
    

