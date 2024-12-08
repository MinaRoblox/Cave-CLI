from gameEngineLibraries import *
from sprites import *

#############
# Things

future_x = 0
future_y = 0

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
        future_x, future_y = Positions.player_posX, Positions.player_posY

        game_board[Positions.player_posX][Positions.player_posY] = "0"
        """
        
        Alright, so there is some black magic that makes it so that posX and posY
        are switched. So the code is reversed so that if it moves up, the posX variable
        is changed.
        
        """
        if (direction == "w" or direction == "W") and Positions.player_posX > 0:
            future_x -= 1

        if (direction == "s" or direction == "S") and Positions.player_posX < 6:
            future_x += 1

        if (direction == "a" or direction == "A") and Positions.player_posY > 0:
            future_y -= 1

        if (direction == "d" or direction == "D") and Positions.player_posY < 6:
            future_y += 1

        Positions.player_posX = future_x
        Positions.player_posY = future_y

        game_board[Positions.player_posX][Positions.player_posY] = player_design


class Positions:
    player_posX, player_posY = 3, 3

    # First row of bP are the left side.
    # Second row of bP are the center up side.
    # Third row of bP are the right side.
    # Fourth and last row are the center down side. 
    bordersPositions = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6),
                        (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0),
                        (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6),
                        (1, 6), (2, 6), (3, 6), (4, 6), (5, 6)]

def gameLoop():
    while True:
        Functions.gameBoardShower()
        print("Input a valid direction!")
        playerDir = Functions.playerInputReceiver()

        if playerDir == "q" or playerDir == "Q":
            os.system("clear")
            exit()

        elif debugMode == True:
            print(f"The letter '{playerDir}' was typed.")

        Functions.movePlayer(playerDir)
        os.system("clear")

if __name__ == '__main__':
    gameLoop()