from typing import Tuple
import clingo


class Sudoku:
    def __init__(self, sudoku: dict[Tuple[int, int], int]):
        self.sudoku = sudoku

    def __str__(self) -> str:
        s = ""
        
        for row in range(1, 10):
            if row > 1 and (row - 1) % 3 == 0:
                s += "\n"

            for col in range(1, 10):
                s += str(self.sudoku[(row, col)])

                if col < 9:
                    if col % 3 == 0:
                        s += "  "
                    else:
                        s += " "

            if row < 9:
                s += "\n"

        return s

    @classmethod
    def from_str(cls, s: str) -> "Sudoku":
        sudoku = {}
        # YOUR CODE HERE
        return cls(sudoku)

    @classmethod
    def from_model(cls, model: clingo.solving.Model) -> "Sudoku":
        sudoku = {}
        
        for symbol in model.symbols(shown=True):
            row = symbol.arguments[0].number
            col = symbol.arguments[1].number
            value = symbol.arguments[2].number

            sudoku[(row, col)] = value

        return cls(sudoku)
