# Chain Reaction Game for 2 players

"""The empty squares are the ones with 0 value, Player 1's turn is encoded as positive entries and Player 2's turns are encoded by negative entries"""

#######################################################################################################################################################################
from fractions import Fraction

# Generating a 2D grid of a given size
def grid_design(nrows,ncols):
    grid=[0]*nrows
    for i in range(nrows):
        grid[i] = [0]*ncols
    return grid

# Printing the grid
def print_grid(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(str(Fraction(matrix[i][j])),sep=" ",end=" ",flush=True)
        print("\n")

# Returns the minimum and index of the minimum in the grid
def min_grid(matrix):
    min_list = [0]*len(matrix)
    for i in range(len(matrix)):
        min_list[i] = min(matrix[i])
    row_ind = min_list.index(min(min_list))
    col_ind = matrix[row_ind].index(min(matrix[row_ind]))
    return (min(min_list),(row_ind,col_ind))

# Returns the maximum and index of the maximum in the grid
def max_grid(matrix):
    max_list = [0]*len(matrix)
    for i in range(len(matrix)):
        max_list[i] = max(matrix[i])
    row_ind = max_list.index(max(max_list))
    col_ind = matrix[row_ind].index(max(matrix[row_ind]))
    return (max(max_list),(row_ind,col_ind))
    
# Identifying the affected neighbors if the user selects the location (x,y)
def aff_sqrs(matrix,x,y):
    if (x==0 and y==0):
        sqrs = [(0,1),(1,0)]
    elif (x==len(matrix)-1 and y==0):
        sqrs = [(x-1,0),(x,1)]
    elif (x==0 and y==len(matrix[0])-1):
        sqrs = [(0,y-1),(1,y)]
    elif (x==len(matrix)-1 and y==len(matrix[0])-1):
        sqrs = [(x-1,y),(x,y-1)]
    elif x==0:
        sqrs = [(x,y-1),(x+1,y),(x,y+1)]
    elif x==len(matrix)-1:
        sqrs = [(x,y-1),(x-1,y),(x,y+1)]
    elif y==0:
        sqrs = [(x-1,y),(x+1,y),(x,y+1)]
    elif y==len(matrix[0])-1:
        sqrs = [(x-1,y),(x+1,y),(x,y-1)]
    else:
        sqrs = [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]
    return sqrs

# Taking player's inputs on turns
def player_turn(matrix,i):
    """ i can only take value 1 and 2, it is an internal parameter"""
    while True:
        (x,y)= input("Enter the location for putting your colored ball in the grid in numbers or type e twice to exit the game: ")
        if x=="e" and y=="e":
            return "e"
        else:
            x=int(x)
            y=int(y)
            if 0<=x<len(matrix) and 0<=y<len(matrix[0]):
                if (i==1 and matrix[x][y]>=0) or (i==2 and matrix[x][y]<=0):
                    return (x,y)
                elif i==1:
                    print("The entered location is already occupied by a negative integer")
                    print_grid(matrix)
                    print("You can enter locations which have a non-negative value")
                elif i==2:
                    print("The entered location is already occupied by a positive integer")
                    print_grid(matrix)
                    print("You can enter locations which have a non-positive value")
                else:
                    print("The entered location is out of range, " + "x should be < " + str(len(matrix)) + " and y should be < " + str(len(matrix[0])))


# Scoring function for a turn
def update_score(matrix,x,y,i):
    if i==1:
        if (x==0 and y==0) or (x==len(matrix)-1 and y==0) or (x==0 and y==len(matrix[0])-1) or (x==len(matrix)-1 and y==len(matrix[0])-1):
            if matrix[x][y] >= 1:
                matrix[x][y]=0
                sqrs = aff_sqrs(matrix,x,y)
                for j in range(len(sqrs)):
                    matrix[sqrs[j][0]][sqrs[j][1]] = abs(matrix[sqrs[j][0]][sqrs[j][1]]) + Fraction(1,2)
            else:
                matrix[x][y] = matrix[x][y] + Fraction(1,2)
        elif x==0 or x==len(matrix)-1:
            if matrix[x][y] >= 1:
                matrix[x][y]=0
                sqrs = aff_sqrs(matrix,x,y)
                for j in range(len(sqrs)):
                    matrix[sqrs[j][0]][sqrs[j][1]] = abs(matrix[sqrs[j][0]][sqrs[j][1]]) + Fraction(1,3)
            else:
                matrix[x][y] = matrix[x][y] + Fraction(1,3)
        elif y==0 or y==len(matrix[0])-1:
            if matrix[x][y] >= 1:
                matrix[x][y]=0
                sqrs = aff_sqrs(matrix,x,y)
                for j in range(len(sqrs)):
                    matrix[sqrs[j][0]][sqrs[j][1]] = abs(matrix[sqrs[j][0]][sqrs[j][1]]) + Fraction(1,3)
            else:
                matrix[x][y] = matrix[x][y] + Fraction(1,3)
        else:
            if matrix[x][y] >= 1:
                matrix[x][y]=0
                sqrs = aff_sqrs(matrix,x,y)
                for j in range(len(sqrs)):
                    matrix[sqrs[j][0]][sqrs[j][1]] = abs(matrix[sqrs[j][0]][sqrs[j][1]]) + Fraction(1,4)
            else:
                matrix[x][y] = matrix[x][y] + Fraction(1,4)
    elif i==2:
        if (x==0 and y==0) or (x==len(matrix)-1 and y==0) or (x==0 and y==len(matrix[0])-1) or (x==len(matrix)-1 and y==len(matrix[0])-1):
            if matrix[x][y] <= -1:
                matrix[x][y]=0
                sqrs = aff_sqrs(matrix,x,y)
                for j in range(len(sqrs)):
                    if matrix[sqrs[j][0]][sqrs[j][1]]<0:
                        matrix[sqrs[j][0]][sqrs[j][1]] = matrix[sqrs[j][0]][sqrs[j][1]] - Fraction(1,2)
                    else:
                        matrix[sqrs[j][0]][sqrs[j][1]] = -matrix[sqrs[j][0]][sqrs[j][1]] - Fraction(1,2)
            else:
                matrix[x][y] = matrix[x][y] - Fraction(1,2)
        elif x==0 or x==len(matrix)-1:
            if matrix[x][y] <= -1:
                matrix[x][y]=0
                sqrs = aff_sqrs(matrix,x,y)
                for j in range(len(sqrs)):
                    if matrix[sqrs[j][0]][sqrs[j][1]]<0:
                        matrix[sqrs[j][0]][sqrs[j][1]] = matrix[sqrs[j][0]][sqrs[j][1]] - Fraction(1,3)
                    else:
                        matrix[sqrs[j][0]][sqrs[j][1]] = -matrix[sqrs[j][0]][sqrs[j][1]] - Fraction(1,3)
            else:
                matrix[x][y] = matrix[x][y] - Fraction(1,3)
        elif y==0 or y==len(matrix[0])-1:
            if matrix[x][y] <= -1:
                matrix[x][y]=0
                sqrs = aff_sqrs(matrix,x,y)
                for j in range(len(sqrs)):
                    if matrix[sqrs[j][0]][sqrs[j][1]]<0:
                        matrix[sqrs[j][0]][sqrs[j][1]] = matrix[sqrs[j][0]][sqrs[j][1]] - Fraction(1,3)
                    else:
                        matrix[sqrs[j][0]][sqrs[j][1]] = -matrix[sqrs[j][0]][sqrs[j][1]] - Fraction(1,3)
            else:
                matrix[x][y] = matrix[x][y] - Fraction(1,3)
        else:
            if matrix[x][y] <= -1:
                matrix[x][y]=0
                sqrs = aff_sqrs(matrix,x,y)
                for j in range(len(sqrs)):
                    if matrix[sqrs[j][0]][sqrs[j][1]]<0:
                        matrix[sqrs[j][0]][sqrs[j][1]] = matrix[sqrs[j][0]][sqrs[j][1]] - Fraction(1,4)
                    else:
                        matrix[sqrs[j][0]][sqrs[j][1]] = -matrix[sqrs[j][0]][sqrs[j][1]] - Fraction(1,4)
            else:
                matrix[x][y] = matrix[x][y] - Fraction(1,4)
    while min_grid(matrix)[0]<=-1:
        update_score(matrix,min_grid(matrix)[1][0],min_grid(matrix)[1][1],i)
    while max_grid(matrix)[0]>=1:
        update_score(matrix,max_grid(matrix)[1][0],max_grid(matrix)[1][1],i)
    return matrix

# Playing a round which involves a turn each
def rounds(matrix,i):
    pt = player_turn(matrix,i)
    if isinstance(pt[0],str):
        return pt
    else:
        update_matrix = update_score(matrix,pt[0],pt[1],i)
        return update_matrix

# Declaring the winner
def result(matrix):
    if min_grid(matrix)[0]==0:
        print_grid(matrix)
        return print("Player 1 wins the Game")
    elif max_grid(matrix)[0]==0:
        print_grid(matrix)
        return print("Player 2 wins the Game")
    else:
        print_grid(matrix)
        return 0
        
# The game function
def ChainReaction(matrix):
    print_grid(matrix)
    print("\n")
    matrix = rounds(matrix,1)
    if isinstance(matrix,list)==False:
        return print("Player 1 ended the game")
    else:
        print_grid(matrix)
        print("\n")
        matrix = rounds(matrix,2)
        if isinstance(matrix,list)==False:
            return print("Player 2 ended the game")
    while True:
        print_grid(matrix)
        print("\n")
        matrix = rounds(matrix,1)
        if isinstance(matrix,list)==False:
            return print("Player 1 ended the game")
        else:
            out=result(matrix)
            if out==0:
                matrix = rounds(matrix,2)
                if isinstance(matrix,list)==False:
                    return print("Player 2 ended the game")
                else:
                    out=result(matrix)
                    if out!=0:
                        return out
            else:
                return out

# Playing the game
grid=grid_design(8,6)
ChainReaction(grid)
