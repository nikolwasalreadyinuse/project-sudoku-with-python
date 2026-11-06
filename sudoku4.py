import sys
import clingo
from sudoku_board import Sudoku


class ClingoApp(clingo.application.Application):
    def print_model(self, model, printer):
        sudoku = Sudoku.from_model(model)
        print(sudoku)
            

    def main(self, ctl, files):
        ctl.load("sudoku.lp")

        for f in files:
            ctl.load(f)

        if not files:
            ctl.load("-")

        ctl.ground([("base", [])])
        ctl.solve(on_model=lambda model: self.print_model(model, None))

if __name__ == "__main__":
    clingo.application.clingo_main(ClingoApp())
    
