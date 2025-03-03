from player import Player

class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.__board = []

        for i in range(width):
            self.__board.append([])
            for j in range(height):
                self.__board[i].append(" ")

    def add_token(self, column, token):
        for i in range(self.height - 1, -1, -1):
            if self.__board[column][i] == " ":
                self.__board[column][i] = token
                return
            if i == 0 and self.__board[column][i] != " ":
                print("This column is full!")
                return

    
    def __str__(self):
        string = ""
        for i in range(self.height):
            for j in range(self.width):
                string += f"| {self.__board[j][i]} "
                if j == self.width - 1:
                    string += "|\n"
        return string
    


board = Board(7, 6)

print(board)

board.add_token(2, "o")
board.add_token(4, "o")

board.add_token(4, "*")
board.add_token(5, "*")
board.add_token(5, "*")
board.add_token(5, "*")
board.add_token(5, "*")
board.add_token(5, "*")
board.add_token(5, "*")
board.add_token(5, "*")
board.add_token(5, "*")
board.add_token(5, "*")

print(board)