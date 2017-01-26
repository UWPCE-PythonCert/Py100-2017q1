def grid_printer(gridsize, cellsize):

    #build horrible lines that you should be ashamed of
    horiz_dashes = (cellsize * '- ') 
    horiz_line = ( '+ ' + horiz_dashes) * gridsize + '+'
    vert_dashes = ('| ' + ('  ' * cellsize)) * gridsize + '|'
    
#build for loops based on your total line count size
    
    #yeah, we have to build a special usecase to handle if cell size is one so that it draws correctly :-/
    if cellsize == 1:
        for i in range(0,gridsize):
            if i == 0:
                print(horiz_line)
                print(vert_dashes)
                print(horiz_line)

            elif i % 2 == 0 and i == gridsize-1:
                print(vert_dashes)
                print(horiz_line)

            elif i % 2 == 0:
                print(vert_dashes)

            elif i % 2 != 0:
                print(vert_dashes)
                print(horiz_line)

    #the less embarassing usecase
    else:
        for i in range(0,cellsize*gridsize):
            #on the non vert lines print both a horizontal and vert line, because otherwise the count is off and you end up short
            if i % cellsize == 0:
                print(horiz_line)
                print(vert_dashes)

            #for the last run through the range make sure you print one last vert line before you print the horizontal line
            elif i == cellsize*gridsize-1:
                print(vert_dashes)
                print(horiz_line)

            else:
                print(vert_dashes)

if __name__ == '__main__':
    #run grid printer with the args of your choice
    #yeah we could get creative with argparse, but thats not really the point of this exercise
    grid_printer(9, 2)