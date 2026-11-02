% Define rows, columns, and digits from 1 to 9.
row(1..9).
col(1..9).
num(1..9).

% Every cell must contain exactly one digit.
1 { sudoku(R,C,N) : num(N) } 1 :- row(R), col(C).

% All given clues must be preserved.
:- initial(R,C,N), not sudoku(R,C,N).

% No digit can appear twice in the same row.
:- sudoku(R,C1,N), sudoku(R,C2,N), C1 < C2.

% No digit can appear twice in the same column.
:- sudoku(R1,C,N), sudoku(R2,C,N), R1 < R2.

% Identify each 3x3 box.
box(R,C,(R-1)/3,(C-1)/3) :- row(R), col(C).

% No digit can appear twice in the same 3x3 box.
:- sudoku(R1,C1,N), sudoku(R2,C2,N), R1 < R2,
   box(R1,C1,BR,BC), box(R2,C2,BR,BC).

% Display only the completed Sudoku cells.
#show sudoku/3.