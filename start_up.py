from board import *

# create root window
root = Tk()
root.title('Math puzzle')
# root.geometry("900x800")
root.iconbitmap('puzzle.ico')

# Generates puzzle board. Definition in board.py
generate_board(root)


root.mainloop()
