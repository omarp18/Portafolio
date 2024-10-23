
public class XOJuego {
    public static final char[][] Board = null;
	char[][] board;
    private char playeract;

    public XOJuego() {
        board = new char[3][3];
        playeract='X'; // Comienza el primer jugador (X)
        initBoard();
    }

    public void initBoard() {
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                board[i][j] = ' ';
            }
        }
    }

    public void printBoard() {
        System.out.println("  1 2 3");
        for (int i = 0; i < 3; i++) {
            System.out.print(i + 1 + " ");
            for (int j = 0; j < 3; j++) {
                System.out.print(board[i][j] + " ");
            }
            System.out.println();
        }
    }

    public boolean Boardlleno() {
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                if (board[i][j] == ' ') {
                    return false;
                }
            }
        }
        return true;
    }

   
    public boolean makeMove(int row, int col) {
        if (row >= 0 && row < 3 && col >= 0 && col < 3 && board[row][col] == ' ') {
            board[row][col] = playeract;
            return true;
        }
        return false;
    }

    public char getplayeract() {
        return playeract;
    }

    public void switchPlayer() {
        playeract = (playeract == 'X') ? 'O': 'X';
    }
}