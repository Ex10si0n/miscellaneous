package comp212.courselab.Exercises;

import java.util.ArrayList;

import static java.lang.Integer.max;

public class ArrayTest2 {
    public static void main(String[] args) {
        int n = 4;
        int[][] arr = {{0, 0, 1, 1}, {0, 0, 1, 1}, {1, 1, 0, 1}, {1, 0, 1, 0}};
        ArrayList<Integer> row = new ArrayList<Integer>();
        ArrayList<Integer> col = new ArrayList<Integer>();
        int maxRowsCnt = 0;
        int maxColsCnt = 0;
        for (int i = 0; i < 4; i++) {
            int rowsCnt = 0;
            for (int j = 0; j < 4; j++) {
                rowsCnt += arr[i][j];
            }
            maxRowsCnt = max(rowsCnt, maxRowsCnt);
        }
        for (int i = 0; i < 4; i++) {
            int colsCnt = 0;
            for (int j = 0; j < 4; j++) {
                colsCnt += arr[j][i];
            }
            maxColsCnt = max(colsCnt, maxColsCnt);
        }
        for (int i = 0; i < 4; i++) {
            int rowsCnt = 0;
            for (int j = 0; j < 4; j++) {
                rowsCnt += arr[i][j];
            }
            if (rowsCnt == maxRowsCnt) {
                row.add(i);
            }
        }
        for (int i = 0; i < 4; i++) {
            int colsCnt = 0;
            for (int j = 0; j < 4; j++) {
                colsCnt += arr[j][i];
            }
            if (colsCnt == maxColsCnt) {
                col.add(i);
            }
        }
        System.out.println(row);
        System.out.println(col);
    }
}
