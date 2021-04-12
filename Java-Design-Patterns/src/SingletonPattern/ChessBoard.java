package SingletonPattern;

public class ChessBoard {
    private static ChessBoard instance = new ChessBoard();

    private ChessBoard() {
    }

    public static ChessBoard getInstance() {
        return instance;
    }

    public void showChessBoard() {
        for (int i = 0; i < 8; i++) {
            for (int j = 0; j < 8; j++) {
                if (i % 2 == 0) {
                    if (j % 2 == 0) System.out.print("⬛");
                    else System.out.print("⬜️");
                } else {
                    if (j % 2 == 0) System.out.print("⬜️");
                    else System.out.print("️⬛");
                }
            }
            System.out.println();
        }
    }
}
