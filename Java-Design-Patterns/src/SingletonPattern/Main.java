package SingletonPattern;

public class Main {
    public static void main(String[] args) {
        ChessBoard chessBoard = ChessBoard.getInstance();
        chessBoard.showChessBoard();
    }
}
