import os

class ConnectFour:

    def __init__(self, board=[0 for i in range(7*6)], player_id=1):
        self.board = board
        self.player_id = player_id

    def GetPlayerId(self):
        """Returns current player."""
        return self.player_id


    def GetBoard(self):
        """Returns current board."""
        return self.board

    def IsDraw(self):
        """Returns True if the entire top row is full."""
        counter = 0

        for i in range(7):
            if self.board[i] != 0:
                counter += 1
        if counter >= 7:
            return True
        return False

    def PrintBoard(self):
        """Prints enitre game board."""
        for index, id in enumerate(self.board):
            if index % 7 == 0:
                print("")
            
            if self.board[index] == 1:
                print(" \N{Large Green Circle}", end="   ")
            elif self.board[index] == 2:
                print(" \N{Large Red Circle}", end="   ")
            else:
                print(" \N{Medium White Circle}", end="   ")

        print(f'\n\n  A     B     C     D     E     F     G')

    def HorizontalCheck(board, player_id):
        """Checks all rows for a winning condition."""
        counter = 0

        for index, id in enumerate(board):
            
            if index != 0 and index % 7 == 0:        # Sets counter for new row
                counter = 0
            
            if id == player_id:
                counter += 1
            else:                                    # Checks for continuity
                counter = 0
        
            if counter >= 4:                         # player_id wins
                return True
        return False


    def VerticalCheck(board, player_id):
        """Checks all columns for a winning condition"""
        counter = 0

        for index in range(len(board)):
            if index == 21:                                    # Stops needless checks
                return False
            
            for row in range(4):

                if board[index+row*7] == player_id:            # Column check
                    counter += 1
                else:
                    counter = 0

                if counter >= 4:
                    return True
            counter = 0


    def DiagonalCheck(board, player_id, is_flipped = False):
        """Checks right diagonals and calls FlipBoard to check left diagonals for a winning condition."""
        
        def FlipBoard(board):     
            newboard = []

            for row in range(6):
                for index in range(7, 0, -1):
                    newboard.append(board[index+(row*7)-1])
            return newboard
            
         
        counter = 0

        for index in range(len(board)):

            if index == 18:                                    # Stop needless checks
                if is_flipped == False:
                    flipped_board = FlipBoard(board)
                    is_flipped = True
                    if (ConnectFour.DiagonalCheck(flipped_board, player_id, is_flipped) == True):
                        return True
                    else:
                        return False
                else:
                    return False
            plus = 0
            for row in range(4):
                #print(f'Checking index {plus+index+(row*7)} | {board[plus+index+(row*7)]} | Current Row: {row}')

                if board[plus+index+(row*7)] == player_id:
                    counter += 1
                else:
                    counter = 0
                plus += 1

                if counter >= 4:
                    return True
            counter = 0


    def Checks(self):
        """Calls each check for a winning condition"""
        if ConnectFour.HorizontalCheck(self.board, self.player_id) == True:
            return True
        elif ConnectFour.VerticalCheck(self.board, self.player_id) == True:
            return True
        elif ConnectFour.DiagonalCheck(self.board, self.player_id) == True:
            return True


    def PlaceChip(self):
        """Lets the current player place a chip."""
        letter = ["A", "B", "C", "D", "E", "F", "G"]
        print(f'Player {ConnectFour.GetPlayerId(self)} place your chip!')

        player_input = input()

        for index, id in enumerate(letter):
            if player_input.upper() == id:                                     # Get column
                column = index

        if self.board[column] != 0:                                            # Column is full
            print(f'Column {player_input.upper()} is full!')
            ConnectFour.PlaceChip(self)                                        # Builds stack until chosen column is not full
        else:
            for row in range(6):
                if self.board[column+(row*7)] != 0:
                    self.board[column+((row-1)*7)] = self.player_id
                    return
                
                if row == 5:
                    self.board[column+(row*7)] = self.player_id
                    return


    def NextTurn(self):
        """Switches the current player when called."""
        if self.player_id == 1:
            self.player_id = 2
            return
        
        if self.player_id == 2:
            self.player_id = 1
            return


def main():
    Game = ConnectFour()
    win = False
    is_drawn = False
    while win == False:

        os.system('cls')

        Game.PrintBoard()

        Game.PlaceChip()

        if Game.Checks() == True:
            win = True
        elif Game.IsDraw() == True:
            win = True
            is_drawn = True
        else:    
            Game.NextTurn()
    if is_drawn == True:
        print("The game has been drawn, no one wins!")
    else:
        print(f'Player {Game.GetPlayerId()} has won!')


if __name__ == "__main__":
    main()
