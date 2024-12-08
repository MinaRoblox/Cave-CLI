from gEL import *

class Levels:
    def menu():
        def starter_menu():
            while True:
                print(f"""

                Cave-CLI.
                Made by MinaRoblox.
                        
                Availible commands are:
                        
                play
                help
                exit
                            
                {mandatory_message}

                """)

                what_to_do = input(">>> ")

                if what_to_do == "play":
                    os.system("clear")
                    playG = True
                    break

                elif what_to_do == "help":
                    os.system("clear")
                    print("""

                    In this game, the story isn't developed
                    yet.
                                
                    """)
                            
                    kldsfngijodsfhgoiefsng = input("Press enter to continue >>>")
                        
                elif what_to_do == "exit":
                    os.system("clear")
                    confirm_exit = input("Type exit again to confirm: ")
                    if confirm_exit == "exit":
                        os.system("clear")
                        print("See ya.")
                        exit()

                os.system("clear")

            if playG:
                Levels.Level1()
        
        starter_menu()

    def Level1():
        #############
        # Things

        future_x = 0
        future_y = 0
        collistion = True
        playG = False

        #############

        class Functions:
            def type_write(sentence, type_delay):
                # Save the terminal settings
                fd = sys.stdin.fileno()
                old_settings = termios.tcgetattr(fd)

                try:
                    # Set terminal to raw mode (disables input)
                    tty.setraw(sys.stdin.fileno())
                    
                    # Loop through each character and print the sentence
                    for char in sentence:
                        sys.stdout.write(char)
                        sys.stdout.flush()

                        if char == '\n':
                            sys.stdout.write('\r')  # Return to the beginning of the line

                        time.sleep(type_delay)

                    time.sleep(1)

                finally:
                    # Restore the terminal settings
                    termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
            def playerInputReceiver(): # Ignore this variable.
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
            def StrToIntSummerToStr(str1, str2):
                return str(int(str1) + int(str2))

            def gameBoardShower(): # Somewhat important.
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
                global specials_design, player_design
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
                if (future_y, future_x) not in Positions.bordersPositions:  # Match format
                    Positions.player_posX, Positions.player_posY = future_x, future_y
                    collision = False
                else:
                    collision = True

                if (future_x, future_y) == (Positions.special1_posX, Positions.special1_posY):
                    New_specials_design = Functions.StrToIntSummerToStr(player_design, specials_design)
                    specials_design = New_specials_design
                    player_design = New_specials_design
                else:
                    Positions.player_posX, Positions.player_posY = future_x, future_y
                    specials_design = "3"
                    player_design = "1"
                    collision = False
                    
                if debugMode or productionMode:
                    # Debugging
                    print(f"Future Position: ({future_x}, {future_y})")
                    print(f"Collision Detected: {collision}")

                # Update game board
                game_board[current_x][current_y] = "0"  # Clear the old position
                game_board[Positions.player_posX][Positions.player_posY] = player_design

        class Positions:
            player_posX, player_posY = 7, 4

            # First row of bP are the left side.
            # Second row of bP are the center up side.
            # Third row of bP are the right side.
            # Fourth and last row are the center down side.
            # The rest are walls. 
            bordersPositions = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8),
                                (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0), (8, 0),
                                (8, 1), (8, 2), (8, 3), (8, 4), (8, 5), (8, 6), (8, 7), (8, 8),
                                (1, 8), (2, 8), (3, 8), (4, 8), (5, 8), (6, 8), (7, 8),
                                (3, 6), (3, 7), (2, 6), (1, 6), (5, 6), (6, 6), (7, 6), (5, 7),
                                (3, 3), (2, 3), (1, 3), (6, 3), (6, 2), (6, 1)]
            
            special1_posX, special1_posY = 2, 2

        class Specials:
            """
            
            Specials 1: Guy at the entrance of the cave
            
            """

            special1_posX = Positions.special1_posX
            special1_posY = Positions.special1_posY

            def drawSpecials(specialPosX, specialPosY):
                 game_board[specialPosX][specialPosY] = specials_design

            drawSpecials(special1_posX, special1_posY)

        class Menu:
            def gameLoop():
                while True:
                    Functions.gameBoardShower()
                    print("Input a valid direction!")
                    playerDir = Functions.playerInputReceiver()

                    if playerDir == "q" or playerDir == "Q":
                        os.system("clear")
                        exit()

                    Functions.movePlayer(playerDir)
                    Specials.drawSpecials(Specials.special1_posX, Specials.special1_posY)
                    os.system("clear")

        Menu.gameLoop()        
    
if __name__ == "__main__":
    if debugMode:
        print("Choose level to play:")
        print("0. Menu")
        print("1. Level 1")
        choice = input(">>> ")
        choice = int(choice)

        if choice == 0:
            Levels.menu()
        elif choice == 1:
            Levels.Level1()

    elif productionMode:
        Levels.Level1()

    else:
        Levels.menu()