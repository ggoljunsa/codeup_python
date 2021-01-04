num = int(input())
board = [['*', 'x', '*'],[' ', 'x', 'x'], ['*', ' ', '*']]
for i in range(3): # horizontal output
    for n in range(num): # horizontal multiple
        for j in range(3): # vertical 
            for k in range(num): # vertical multiple
                print(board[i][j], end = '')
        print()