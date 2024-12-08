from gameEngineLibraries import *
from sprites import *

#############
# Things

future_x = 0
future_y = 0
collistion = True

#############

class Functions:
    def playerInputReceiver():
        # Save the terminal settings
        old_settings = termios.tcgetattr(sys.stdin)
        try:
            # Change the terminal settings to raw mode (disable line buffering)
            tty.setraw(sys.stdin.fileno())
            # Read a single character from the input
            char = sys.stdin.read(1)
        finally:
            # Restore the original terminal settings
            termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)
        return char

    def gameBoardShower():
        game_board[Positions.player_posX][Positions.player_posY] = player_design
        def printGameBoard():
            for line in game_board:
                print(" ".join(line))

        def drawBorders():
            for x, y in Positions.bordersPositions:
                game_board[y][x] = border_design

        drawBorders()
        printGameBoard()

    def movePlayer(direction):
        global future_x, future_y
        current_x, current_y = Positions.player_posX, Positions.player_posY
        future_x, future_y = current_x, current_y

        # Determine the future position based on direction
        if (direction == "w" or direction == "W") and current_x > 0:
            future_x -= 1
        elif (direction == "s" or direction == "S") and current_x < len(game_board) - 1:
            future_x += 1
        elif (direction == "a" or direction == "A") and current_y > 0:
            future_y -= 1
        elif (direction == "d" or direction == "D") and current_y < len(game_board[0]) - 1:
            future_y += 1

        # Check for collision with borders
        if (future_x, future_y) not in Positions.bordersPositions:
            # No collision, update player position
            Positions.player_posX, Positions.player_posY = future_x, future_y
            collistion = False
        else:
            # Collision detected, retain current position
            collistion = True

        # Update game board
        game_board[current_x][current_y] = "0"  # Clear the old position
        game_board[Positions.player_posX][Positions.player_posY] = player_design


class Positions:
    player_posX, player_posY = 4, 4

    # First row of bP are the left side.
    # Second row of bP are the center up side.
    # Third row of bP are the right side.
    # Fourth and last row are the center down side. 
    bordersPositions = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8),
                        (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0), (8, 0),
                        (8, 1), (8, 2), (8, 3), (8, 4), (8, 5), (8, 6), (8, 7), (8, 8),
                        (1, 8), (2, 8), (3, 8), (4, 8), (5, 8), (6, 8), (7, 8)]

def gameLoop():
    while True:
        Functions.gameBoardShower()
        print("Input a valid direction!")
        playerDir = Functions.playerInputReceiver()

        if playerDir == "q" or playerDir == "Q":
            os.system("clear")
            exit()

        Functions.movePlayer(playerDir)
        os.system("clear")

if __name__ == '__main__':
    gameLoop()