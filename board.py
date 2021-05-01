from tkinter import *
from constants import *
from helper import *
import threading
from tkinter import messagebox
import time

# Create our matches
matches = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Shuffle our matches
random.shuffle(matches)

# Define our puzzle entries
my_entries = []

# Generate our operations and save them in a list. Indexes are described in the helper.py
my_operators = generate_operators()


def generate_board(root):
    # Timer label. Play button triggers timer function, which updates this label
    my_timer = Label(root, text="", font=timer_font, fg=timer_color)
    my_timer.pack(pady=20)

    # Create puzzle frame
    puzzle_board = Frame(root)
    puzzle_board.pack(pady=20)

    # Instructions are packed to the root directly after the puzzle board, thus appear at the bottom
    label_instructions = Label(root, text=instructions, font=label_font, fg=instructions_color)
    label_instructions.pack(pady=20, padx=20)

    # Row Loop (step of 2 leaves space for the horizontal operator)
    for r in range(0, 5, 2):
        # Column Loop (step of 2 leaves space for the vertical operator)
        for c in range(0, 5, 2):
            entry_text = Text(puzzle_board, height=height_size, width=width_size, font=large_font, bd=border_size,
                              padx=x_pad,
                              pady=y_pad)
            entry_text.grid(row=r, column=c)
            my_entries.append(entry_text)

    # Loop?
    create_sign_label(0, 0, 1, puzzle_board)
    create_sign_label(1, 0, 3, puzzle_board)
    create_sign_label(2, 2, 1, puzzle_board)
    create_sign_label(3, 2, 3, puzzle_board)
    create_sign_label(4, 4, 1, puzzle_board)
    create_sign_label(5, 4, 3, puzzle_board)
    create_sign_label(6, 1, 0, puzzle_board)
    create_sign_label(7, 3, 0, puzzle_board)
    create_sign_label(8, 1, 2, puzzle_board)
    create_sign_label(9, 3, 2, puzzle_board)
    create_sign_label(10, 1, 4, puzzle_board)
    create_sign_label(11, 3, 4, puzzle_board)

    # Calculate rows and cols results
    # Loop?
    ABC = calc_result(matches[0], matches[1], matches[2], my_operators[0], my_operators[1])
    DEF = calc_result(matches[3], matches[4], matches[5], my_operators[2], my_operators[3])
    GHI = calc_result(matches[6], matches[7], matches[8], my_operators[4], my_operators[5])

    ADG = calc_result(matches[0], matches[3], matches[6], my_operators[6], my_operators[7])
    BEH = calc_result(matches[1], matches[4], matches[7], my_operators[8], my_operators[9])
    CFI = calc_result(matches[2], matches[5], matches[8], my_operators[10], my_operators[11])

    # Column 6 - Horizontal results
    Label(puzzle_board, text=f' = {ABC}', font=large_font).grid(row=0, column=5)
    Label(puzzle_board, text=f' = {DEF}', font=large_font).grid(row=2, column=5)
    Label(puzzle_board, text=f' = {GHI}', font=large_font).grid(row=4, column=5)

    # Row 6 - Vertical results
    Label(puzzle_board, text=f' = ', font=large_font).grid(row=5, column=0)
    Label(puzzle_board, text=f' = ', font=large_font).grid(row=5, column=2)
    Label(puzzle_board, text=f' = ', font=large_font).grid(row=5, column=4)

    Label(puzzle_board, text=f'{ADG}', font=large_font).grid(row=6, column=0)
    Label(puzzle_board, text=f'{BEH}', font=large_font).grid(row=6, column=2)
    Label(puzzle_board, text=f'{CFI}', font=large_font).grid(row=6, column=4)

    # Submit
    submit = Button(puzzle_board, text='Submit', font=medium_font, command=lambda: check_result(root))
    submit.grid(row=7, column=2, columnspan=1)

    start = Button(puzzle_board, text='Play', font=medium_font)
    start.grid(row=7, column=0, columnspan=1)

    # Attach code below to start button to activate the timer.
    # Current logic activates the timer on program start up

    # , command=lambda: threading.Thread(target=timer, args=[timeout_seconds, submit, start, my_timer, root]).start())

    # Threading for the timeout function! Without it the app freezes each second
    # setDaemon avoids "RuntimeError: main thread is not in main loop"
    t = threading.Thread(target=timer, args=[timeout_seconds, submit, start, my_timer, root])
    t.setDaemon(True)
    t.start()

    # New Game - logic not implemented yet
    # new_game = Button(puzzle_board, text='Restart', state='disabled', font=medium_font, command=lambda: new_game())
    # new_game.grid(row=7, column=4, columnspan=1)


def check_result(root):
    # Uncomment correct values for debug
    # [print(i) for i in matches]

    is_correct = True

    for i in range(len(matches)):
        entry_value = convert_int(my_entries[i].get("1.0", 'end-1c'))

        if entry_value != matches[i]:
            is_correct = False
            break

    if is_correct:
        messagebox.showinfo("Correct", "Good job!!!")
        # Exits the program
        root.destroy()
    else:
        messagebox.showinfo("Incorrect", "Please try again!")


def timer(t, submit, start, my_timer, root):
    # Disable play button
    start.config(state='disabled')

    while t > -1:
        minutes, seconds = divmod(t, 60)
        time_formatted = 'Time left  {:02d}:{:02d}'.format(minutes, seconds)
        my_timer.config(text=time_formatted)
        time.sleep(1)
        t -= 1

    messagebox.showinfo("Time is up!", "Try again")
    submit.config(state='disabled')
    # Exits the program
    root.destroy()
    # new_game.config(state='normal')


# def new_game():
#
#     submit.config(state='normal')
#     start.config(state='disabled')
#     new_game.config(state='disabled')

def create_sign_label(operator_index, row_index, col_index, puzzle_board):
    Label(puzzle_board, text=f'{my_operators[operator_index]}', height=height_size, width=width_size,
          font=medium_font,
          bd=border_size, padx=x_pad,
          pady=y_pad).grid(row=row_index, column=col_index)
