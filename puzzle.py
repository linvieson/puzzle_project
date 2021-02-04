'''
GitHub link: https://github.com/linvieson/puzzle_project.git
This module validates if a game 9x9 board is ready for the start of the game.
'''

def check_horizontals(board: list) -> bool:
    '''
    Return True if numbers on horizontals are all right, else False.
    >>> check_horizontals(["**** ****", "***1 ****", "**  3****", "* 4 2****",\
 "     9 5 ", " 6  83  *", "3   1  **", "  8  2***", "  2  ****"])
    True
    '''
    for line in board:
        seen = []
        for num in line:
            if num not in seen and num != '*' and num != ' ':
                seen.append(num)
            elif num in seen:
                return False
    return True


def check_verticals(board: list) -> bool:
    '''
    Return True if numbers on verticals are all right, else False.
    >>> check_verticals(["**** ****", "***1 ****", "**  3****", "* 4 2****",\
 "     9 5 ", " 6  83  *", "3   1  **", "  8  2***", "  2  ****"])
    True
    '''
    # turn the table 90 degreees clockwise so that columns are rows
    reversed_arr = [[board[lines][ind] for lines in range(len(board[0]))]\
                     for ind in range(len(board))]

    return check_horizontals(reversed_arr)


def check_colors(board: list) -> bool:
    '''
    Return True if numbers of certain colors are all right, else False.
    >>> check_colors(["**** ****", "***1 ****", "**  3****", "* 4 2****",\
 "     9 5 ", " 6  83  *", "3   1  **", "  8  2***", "  2  ****"])
    True
    '''
    new_board = []
    col = 0

    for line in reversed(range(5)):
        color = []
        shade = []

        # take horiontal cells of one color
        shade.extend([board[line + 4][col], board[line + 4][col + 1],\
            board[line + 4][col + 2], board[line + 4][col + 3],\
            board[line + 4][col + 4]])

        # take vertical cells of one color
        color.extend([board[line + 3][col], board[line + 2][col],\
            board[line + 1][col], board[line][col]])

        new_board.extend([color + shade])
        col += 1

    return check_horizontals(new_board)


def validate_board(board: list) -> bool:
    '''
    Return True if a board is ready for the game, else return False.
    >>> validate_board(["**** ****", "***1 ****", "**  3****", "* 4 2****",\
 "     9 5 ", " 6  83  *", "3   1  **", "  8  2***", "  2  ****"])
    True
    >>> validate_board(["**** ****", "***1 ****", "**  3****", "* 4 1****",\
 "     9 5 ", " 6  83  *", "3   1  **", "  8  2***", "  2  ****"])
    False
    '''
    return check_horizontals(board) & check_verticals(board) &\
       check_colors(board)
