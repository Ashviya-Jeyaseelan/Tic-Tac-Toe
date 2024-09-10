print(f""" Welcome to TIC TAC TOE multiplayer game! 
      \n\n RULES: 
      \n\n 1) Player 1 goes first and then  Player 2.
      \n\n 2) The inputs expected are numbers from 1-9. 
      \n\n 3) Along the horizontal, row 1 consists of 1-3, row 2 of 4-6 and row 3 of 7-9 """
      )

board = [" " for space in range(9)]
"""
Function: print_board
Paramaters: None
Purpose: Displays the tic tac toe board
"""


def print_board():
  row1 = f"| {board[0]} | {board[1]} | {board[2]} |"
  row2 = f"| {board[3]} | {board[4]} | {board[5]} |"
  row3 = f"| {board[6]} | {board[7]} | {board[8]} |"

  print()
  print(row1)
  print(row2)
  print(row3)
  print()


"""
Function: player_move
Paramaters: icon Type: String
Purpose: Sets board based on player move
"""


def player_move(icon):  # icon = X icon = O
  number = None

  if icon == "X":
    number = 1
  elif icon == "O":
    number = 2

  if number == 1:  # Player 1 is moving (x is moving)
    print(f" Your turn player {number}")
  else:
    print(f" Your turn player {number}")

  choice = int(input("Enter your move (1-9): ")
               )  # player inputs where they want to put choice

  if board[choice - 1] == " ":
    board[choice - 1] = icon

  else:  # Incase player moves on invalid spot
    while board[
        choice -
        1] != " ":  # if its anything other than a empty spot its invalid
      print()
      print("That space is taken! Please pick another spot")
      print(f"Current player: {number} Current Icon: {icon}")
      choice = int(input("Enter your move (1-9): ")
                   )  # player inputs where they want to put choice
      if board[choice - 1] == " ":
        board[choice - 1] = icon
        break


"""
Function: is_victory
Paramaters: icon Type: String
Purpose: Determines if player has won the game 
"""


def is_victory(icon):

  if ((board[0] == board[1] == board[2] == icon) or  #rows check
      (board[3] == board[4] == board[5] == icon) or  #rows check
      (board[6] == board[7] == board[8] == icon) or  #rows check
      (board[0] == board[3] == board[6] == icon) or  #columns check
      (board[1] == board[4] == board[7] == icon) or  #columns check
      (board[2] == board[5] == board[8] == icon) or  #columns check
      (board[0] == board[4] == board[8] == icon) or  #diagonals check
      (board[2] == board[4] == board[6] == icon)):  #diagonals check

    return True  # someone has won the game
  else:
    return False  # Game is draw


"""
Function: is_draw
Paramaters: icon Type: String
Purpose: Determines if there is draw in the game
"""


def is_draw():
  if " " not in board:
    return True  # is draw
  return False  # not draw


"""
Students will fill out this portion of the loop. 
Basic strucutre of game activity is in here, they will make function call to make the game function properly.
All functions above will be provided. Will walk through each function, and how game works to design game properly. 

"""

while True:

  print_board()

  player_move("X")  # icon = "X"

  print_board()

  if is_victory("X"):
    print("Player X won the game!")
    break

  elif is_draw():
    print("The game is a draw!")
    break

  player_move("O")

  if is_victory("O"):
    print("Player O won the game!")
    break

  elif is_draw():
    print("The game is a draw!")
    break
