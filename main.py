import random,time,copy,pygame,sys
from block import Block
from gui import *

def try_piece(piece,grid,pos):
    failed = False
    time_count = 0
    while not failed:
        #Create a temporary copy of board to see if piece fits
        temp_board = copy.deepcopy(grid) 

        if can_insert(piece.shape, temp_board, pos):

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                    elif event.key == pygame.K_SPACE:
                        piece.direction += 1
                    elif event.key == pygame.K_a:
                        if pos[1] > -1:
                            pos = (pos[0],pos[1]-1)
                    elif event.key == pygame.K_d:
                        if pos[1] < 8:
                            pos = (pos[0],pos[1]+1)
                    elif event.key == pygame.K_s:
                        if pos[0] <17:
                            pos = (pos[0]+1,pos[1])
                    
            piece.rotate()
            time_count += 1

            # 75 gives ideal block falling speed
            if time_count == 75:
                pos = (pos[0]+1,pos[1])
                time_count = 0
        else:
            failed = True
    
    insert_piece(piece.shape,(pos[0]-1,pos[1]))
    update_grid(grid)
            

#The parameter board is for the temporary board 
def can_insert(piece,board,pos): #pos is the position to insert the piece
    for y in range(4):
        for x in range(4):
            if piece[y][x] != 0: #Only replace the ones
                try:
                    if grid[pos[0]+y][pos[1]+x] != 0: #Checking there isn't already a 1 there
                        return False
                    board[pos[0]+y][pos[1]+x] = piece[y][x] #Replace on temp
                    
                except IndexError:  #If there is an index error, it can't be done
                    return False 
    #display(board)
    update_grid(board)
    return True


def insert_piece(piece,pos):
    try:
        for y in range(4):
            for x in range(4):
                if piece[y][x] != 0:
                    grid[pos[0]+y][pos[1]+x] = piece[y][x]

    except IndexError:
        pass
            
    
def display(board):
        print()
        for i in board:
            print(' '.join([str(j) for j in i]))


def reset_board():
    return [[0 for i in range(10)] for j in range(20)]


def is_row_full(grid):
    empty_rows = [i for i,row in enumerate(grid) if 0 not in row]
    for row in empty_rows:
        del grid[row]
        grid.insert(0,[0,0,0,0,0,0,0,0,0,0])


def play():
    while True:
        shapes_list = list(shapes.keys())
        letter = random.choice(shapes_list)
        b = Block(letter)
        b.direction = random.randint(0,4)
        b.rotate()
        x = random.randint(0,6)
        try_piece(b,grid,(0,x))
        update_grid(grid)
        is_row_full(grid)

        # If any row is full (losing case)
        if len([i for i in grid[0] if i!= 0]):
            time.sleep(2)
            return
    
if __name__ == "__main__":
   while True:
        grid = reset_board()
        play()
    



