
COLUMNS = {'A':0,'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7 }

def checkers(players=1,N=8):
    gen_board(N)




def gen_board():
    board = []
    square = 0
    for i in range(8):
        if i < 3:
            other = 'b'
        elif i >= 3 and i < 5:
            other = 'e'
        else:
            other = 'r'
        square = other_piece(square, other)
        board.append(create_row(other,square))
    return board


def print_board(board):
    cols = [0,'A','B','C','D','E','F','G','H'] #Label Columns
    for j in cols:
        print j,
    print
    for num,row in enumerate(board):
        print num + 1,
        for i in row:
            print i,
        print

def create_row(other, square):
    row = []
    for i in range(8):
        square=other_piece(square, other)
        row.append(square)
    return row

def other_piece(square,other):
    if square == 0:square = other
    else: square = 0
    return square

def move_piece(board, loc, move_loc, valid_pieces = None):
    row,col = select_piece(loc)
    if not row: return False
    piece = board[row][col]
    #if piece not in valid_pieces:return False
    new_row,new_col = select_piece(move_loc)
    if not new_row: return False
    #TODO check if valid move
    #TODO check if there is a forced move?
    #TODO check if being kinged
    board[row][col] = 'e'
    board[new_row][new_col] = piece
    return print_board(board)


def move_outcome(row, col, dir):
    """
    :param row: row number as int
    :param col: col number as int
    :param dir: ('up' or 'down', 'left' or 'right', 'move' or 'jump') as a tuple
    :return: new_row, new_col as ints
    """
    pass

def valid_move():
    pass

def required_move(board,player):
    """

    :param board:
    :param player: whose turn it is ('b' or 'r')
    :return: move or moves that are required (jumps) as a list of ((current_pos), (new_pos)) tuples
    """
    paths = []
    frontier=[]
    if player is 'b':
        dir = 1
        other = 'r'
    else:
        dir = -1
        other = 'b'
    #TODO Account for king pieces...relatedly update board after each jump
    for row in range(8):
        for space in range(8):
            if board[row][space] == player:
                jumps = jumper(board,dir,other,row,space)
                if jumps:
                    paths += jumps
    return paths



def jumper(board, dir, other, row, space):
    """if there is a jump, how many jumps???"""
    #TODO account for multiple direction options
    required =[]
    if space < 6:
        if board[row + dir][space + 1] == other and board[row + 2*dir][space + 2] == 'e':
            required.append(((row,space),(row+2*dir, space+2)))
    if space > 2:
        if board[row + dir][space - 1] == other and board[row + 2*dir][space - 2] == 'e':
            required.append(((row,space),(row+2*dir, space-2)))
    return required


def select_piece(loc):
    """
    :param loc: a string with row and column information eg. 'A1' or '8B'
    :return:piece as  a string, row number as int, col number as int
    """
    if len(loc) != 2:
        print "Invalid Location"
        return False, False, False
    if loc[0] in '12345678':
        try:
            row = int(loc[0]) - 1
            col = COLUMNS[loc[1].upper()]
        except: #TODO is this ok?
            print "Invalid Location"
            return False, False, False
    else:
        try:
            row = int(loc[1]) - 1
            col = COLUMNS[loc[0].upper()]
        except:
            print "Invalid Location"
            return False, False, False
    return row,col


###Tests
#print other(0, "w")
#print other('w', 0)
#print create_row("w", 0)
start = gen_board()
#print start
test_board1 = [[0, 'b', 0, 'b', 0, 'b', 0, 'b'], ['b', 0, 'b', 0, 'b', 0, 'b', 0], [0, 'e', 0, 'e', 0, 'e', 0, 'e'], ['e', 0, 'b', 0, 'e', 0, 'e', 0], [0, 'e', 0, 'r', 0, 'e', 0, 'e'], ['r', 0, 'r', 0, 'r', 0, 'r', 0], [0, 'r', 0, 'r', 0, 'r', 0, 'r'], ['r', 0, 'r', 0, 'r', 0, 'r', 0]]
#print_board(test_board1)
#test_board2 = [[0, 'b', 0, 'b', 0, 'b', 0, 'b'], ['b', 0, 'b', 0, 'b', 0, 'b', 0], [0, 'e', 0, 'e', 0, 'e', 0, 'e'], ['e', 0, 'b', 0, 'b', 0, 'e', 0], [0, 'e', 0, 'r', 0, 'e', 0, 'e'], ['r', 0, 'r', 0, 'r', 0, 'r', 0], [0, 'r', 0, 'r', 0, 'r', 0, 'r'], ['r', 0, 'r', 0, 'r', 0, 'r', 0]]
#print_board(test_board2)
test_board3 = [[0, 'e', 0, 'e', 0, 'e', 0, 'e'], ['b', 0, 'b', 0, 'b', 0, 'b', 0], [0, 'e', 0, 'e', 0, 'e', 0, 'e'], ['e', 0, 'b', 0, 'b', 0, 'e', 0], [0, 'e', 0, 'r', 0, 'e', 0, 'e'], ['r', 0, 'r', 0, 'r', 0, 'r', 0], [0, 'r', 0, 'r', 0, 'r', 0, 'r'], ['r', 0, 'r', 0, 'r', 0, 'r', 0]]
print_board(test_board3)
test_board4 = [[0, 'e', 0, 'e', 0, 'e', 0, 'e'], ['b', 0, 'b', 0, 'b', 0, 'b', 0], [0, 'e', 0, 'e', 0, 'e', 0, 'e'], ['e', 0, 'b', 0, 'b', 0, 'e', 0], [0, 'e', 0, 'r', 0, 'r', 0, 'e'], ['r', 0, 'r', 0, 'r', 0, 'r', 0], [0, 'r', 0, 'r', 0, 'r', 0, 'r'], ['r', 0, 'r', 0, 'r', 0, 'r', 0]]
print_board(test_board4)
#print required_move(start, 'b')
#print required_move(test_board1,'r')
#print required_move(test_board2,'r')
print required_move(test_board3,'r')
print required_move(test_board4,'r')
print required_move(start,'r')
#print jumper(test_board1,-1,'b',4,1)
#print jumper(test_board2,-1,'b',4,3)
#print print_board(gen_board())
#print select_piece('B3')
#print select_piece('5d')
#print select_piece('a31')
#print select_piece('9B')
#print move_piece(start, 'B3', 'C4')


