package com.company;
import java.io.*;
import java.util.Scanner;

public class Main {
    public static char[][] map = new char[30][30];
    public static String getWord;
    public static boolean endGame = false, playerNow = false;
    public static boolean[][] isPlayerUp = new boolean[30][30];

    public static void init() {
        for(int i = 1; i <= 9; i++) for(int j = 1; j <= 5; j++) isPlayerUp[j][i] = true;
        for(int i = 1; i <= 9; i++) for(int j = 6; j <= 10; j++) isPlayerUp[j][i] = false;
        map[1][0] = map[0][1] = '一'; map[2][0] = map[0][2] = '二'; map[3][0] = map[0][3] = '三'; map[4][0] = map[0][4] = '四';
        map[5][0] = map[0][5] = '五'; map[6][0] = map[0][6] = '六'; map[7][0] = map[0][7] = '七'; map[8][0] = map[0][8] = '八';
        map[9][0] = map[0][9] = '九'; map[10][0] = map[0][10] = '十'; map[0][0] = '下';
        for(int i = 1; i <= 10; i++) for(int j = 1; j <= 9; j++) map[i][j]='口';
        map[1][1] = map[10][1] = map[1][9] = map [10][9] = '车';
        map[1][2] = map[10][2] = map[1][8] = map [10][8] = '马';
        map[1][3] = map[1][7] = '象';
        map[10][3] = map [10][7] = '相';
        map[1][4] = map[1][6] = '士';
        map[10][4] = map [10][6] = '仕';
        map[1][5] = '帅'; map[10][5] = '将';
        map[3][2] = map[8][2] = map[3][8] = map[8][8] =  '炮';
        map[4][1] = map[4][3] = map[4][5] = map[4][7] = map[4][9] = '卒';
        map[7][1] = map[7][3] = map[7][5] = map[7][7] = map[7][9] = '兵';
    }

    public static void printError() {
        System.out.println("错误的输入");
    }

    public static void printMap() {
        System.out.print(map[0][0] + "     ");
        for(int i = 1; i <= 9; i++) {
            System.out.print(map[i][0] + "  ");
        }
        System.out.println("\n");
        for(int i = 1; i <= 10; i++) {
            System.out.print("       ");
            for(int j = 1; j <= 9; j++) {
                System.out.print(map[i][j] + "  ");
            }
            System.out.println();
        }
        System.out.println();
        System.out.print("       ");
        for(int i = 9; i >= 1; i--) {
            System.out.print(map[i][0] + "  ");
        }

        //打印势力
        if(false){
            System.out.println();
            for(int i = 1; i <= 10; i++) {
                for(int j = 1; j <= 9; j++) {
                    System.out.print(isPlayerUp[i][j] + "  ");
                }
                System.out.println();
            }
        }
    }

    public static void changeRoll() {
        if(map[0][0] == '上') map[0][0] = '下';
        else map[0][0] = '上';
        playerNow = !playerNow;
    }

    public static void run() throws IOException {

        String cnNum = "零一二三四五六七八九";
        String arNum = "0123456789";
        Scanner scanner = new Scanner(System.in);
        getWord = scanner.nextLine();
        char main = (getWord.charAt(0));
        char getStart = (getWord.charAt(1));
        char act = (getWord.charAt(2));
        char getEnd = (getWord.charAt(3));
        int start, end;
        if(Character.isDigit(getStart)){
            start = arNum.indexOf(getStart);
            end = arNum.indexOf(getEnd);
        }else {
            start = cnNum.indexOf(getStart);
            end = cnNum.indexOf(getEnd);
        }

        if(act == '平') {
            if(playerNow == true) {
                for(int i = 1; i <= 10; i++) {
                    if(map[i][start] == main && isPlayerUp[i][start] == playerNow) {
                        map[i][end] = map[i][start];
                        map[i][start] = '口';
                        isPlayerUp[i][end] = isPlayerUp[i][start];
                        isPlayerUp[i][start] = !isPlayerUp[i][start];
                        break;
                    }
                }
            }else {
                for(int i = 1; i <= 10; i++) {
                    if(map[i][10 - start] == main && isPlayerUp[i][10 - start] == playerNow) {
                        map[i][10 - end] = map[i][10 - start];
                        map[i][10 -start] = '口';
                        isPlayerUp[i][10 - end] = isPlayerUp[i][10 - start];
                        isPlayerUp[i][10 - start] = !isPlayerUp[i][10 - start];
                        break;
                    }
                }
            }
        }
        if(act == '进') {
            if(playerNow == false) {
                for(int i = 1; i <= 10; i++) {
                    if(map[i][10 - start] == main && isPlayerUp[i][10 - start] == playerNow) {
                        if(main == '马') {
                            if(Math.abs(start - end) == 1) {
                                map[i - 2][10 - end] = map[i][10 - start];
                                map[i][10 - start] = '口';
                                isPlayerUp[i - 2][10 - end] = isPlayerUp[i][10 - start];
                                isPlayerUp[i][10 - start] = !isPlayerUp[i][10 - start];
                                break;
                            }else if(Math.abs(start - end) == 2) {
                                map[i - 1][10 - end] = map[i][10 - start];
                                map[i][10 - start] = '口';
                                isPlayerUp[i - 1][10 - end] = isPlayerUp[i][10 - start];
                                isPlayerUp[i][10 - start] = !isPlayerUp[i][10 - start];
                                break;
                            }else {
                                printError();
                            }
                        }
                        if(main == '象'|| main == '相') {
                            if(Math.abs(start - end) == 2) {
                                map[i - 2][10 - end] = map[i][10 - start];
                                map[i][10 - start] = '口';
                                isPlayerUp[i - 2][10 - end] = isPlayerUp[i][10 - start];
                                isPlayerUp[i][10 - start] = !isPlayerUp[i][10 - start];
                                break;
                            }else {
                                printError();
                            }
                        }
                        if(main == '士'|| main == '仕') {
                            if(Math.abs(start - end) == 1) {
                                map[i - 1][10 - end] = map[i][10 - start];
                                map[i][10 - start] = '口';
                                isPlayerUp[i - 1][10 - end] = isPlayerUp[i][10 - start];
                                isPlayerUp[i][10 - start] = !isPlayerUp[i][10 - start];
                                break;
                            }else {
                                printError();
                            }
                        }
                        map[i - end][10 - start] = map[i][10 - start];
                        map[i][10 - start] = '口';
                        isPlayerUp[i - end][10 - start] = isPlayerUp[i][10 - start];
                        isPlayerUp[i][10 - start] = !isPlayerUp[i][10 - start];
                        break;
                    }
                }
            }else {
                for (int i = 1; i <= 10; i++) {
                    if (map[i][start] == main && isPlayerUp[i][start] == playerNow) {
                        if(main == '马') {
                            if(Math.abs(start - end) == 1) {
                                map[i + 2][end] = map[i][start];
                                map[i][start] = '口';
                                isPlayerUp[i + 2][end] = isPlayerUp[i][start];
                                isPlayerUp[i][start] = !isPlayerUp[i][start];
                                break;
                            }else if(Math.abs(start - end) == 2) {
                                map[i + 1][end] = map[i][start];
                                map[i][start] = '口';
                                isPlayerUp[i + 1][end] = isPlayerUp[i][start];
                                isPlayerUp[i][start] = !isPlayerUp[i][start];
                                break;
                            }else {
                                printError();
                            }
                        }
                        if(main == '象' || main == '相') {
                            if(Math.abs(start - end) == 2) {
                                map[i + 2][end] = map[i][start];
                                map[i][start] = '口';
                                isPlayerUp[i + 2][end] = isPlayerUp[i][start];
                                isPlayerUp[i][start] = !isPlayerUp[i][start];
                                break;
                            }else {
                                printError();
                            }
                        }
                        if(main == '士' || main == '仕') {
                            if(Math.abs(start - end) == 1) {
                                map[i + 1][end] = map[i][start];
                                map[i][start] = '口';
                                isPlayerUp[i + 1][end] = isPlayerUp[i][start];
                                isPlayerUp[i][start] = !isPlayerUp[i][start];
                                break;
                            }else {
                                printError();
                            }
                        }
                        map[i + end][start] = map[i][start];
                        map[i][start] = '口';
                        isPlayerUp[i + end][start] = isPlayerUp[i][start];
                        isPlayerUp[i][start] = !isPlayerUp[i][start];
                        break;
                    }
                }
            }
        }
        if(act == '退') {
            if (playerNow == false) {
                for (int i = 1; i <= 10; i++) {
                    if (map[i][10 - start] == main && isPlayerUp[i][10 - start] == playerNow) {
                        if(main == '马') {
                            if(Math.abs(start - end) == 1) {
                                map[i + 2][10 - end] = map[i][10 - start];
                                map[i][10 - start] = '口';
                                isPlayerUp[i + 2][10 - end] = isPlayerUp[i][10 - start];
                                isPlayerUp[i][10 - start] = !isPlayerUp[i][10 - start];
                                break;
                            }else if(Math.abs(start - end) == 2) {
                                map[i + 1][10 - end] = map[i][10 - start];
                                map[i][10 - start] = '口';
                                isPlayerUp[i + 1][10 - end] = isPlayerUp[i][10 - start];
                                isPlayerUp[i][10 - start] = !isPlayerUp[i][10 - start];
                                break;
                            }else {
                                printError();
                            }

                        }
                        if(main == '象' || main == '相') {
                            if(Math.abs(start - end) == 2) {
                                map[i + 2][10 - end] = map[i][10 - start];
                                map[i][10 - start] = '口';
                                isPlayerUp[i + 2][10 - end] = isPlayerUp[i][10 - start];
                                isPlayerUp[i][10 - start] = !isPlayerUp[i][10 - start];
                                break;
                            }else {
                                printError();
                            }
                        }
                        if(main == '士'|| main == '仕') {
                            if(Math.abs(start - end) == 1) {
                                map[i + 1][10 - end] = map[i][10 - start];
                                map[i][10 - start] = '口';
                                isPlayerUp[i + 1][10 - end] = isPlayerUp[i][10 - start];
                                isPlayerUp[i][10 - start] = !isPlayerUp[i][10 - start];
                                break;
                            }else {
                                printError();
                            }
                        }
                        map[i + end][10 - start] = map[i][10 - start];
                        map[i][10 - start] = '口';
                        isPlayerUp[i + end][10 - start] = isPlayerUp[i][10 - start];
                        isPlayerUp[i][10 - start] = !isPlayerUp[i][10 - start];
                        break;
                    }
                }
            } else {
                for (int i = 1; i <= 10; i++) {
                    if (map[i][start] == main && isPlayerUp[i][start] == playerNow) {
                        if(main == '马') {
                            if(Math.abs(start - end) == 1) {
                                map[i - 2][end] = map[i][start];
                                map[i][start] = '口';
                                isPlayerUp[i - 2][end] = isPlayerUp[i][start];
                                isPlayerUp[i][start] = !isPlayerUp[i][start];
                                break;
                            }else if(Math.abs(start - end) == 2) {
                                map[i - 1][end] = map[i][start];
                                map[i][start] = '口';
                                isPlayerUp[i - 1][end] = isPlayerUp[i][start];
                                isPlayerUp[i][start] = !isPlayerUp[i][start];
                                break;
                            }else {
                                printError();
                            }

                        }
                        if(main == '象' || main == '相') {
                            if(Math.abs(start - end) == 2) {
                                map[i - 2][end] = map[i][start];
                                map[i][start] = '口';
                                isPlayerUp[i - 2][end] = isPlayerUp[i][start];
                                isPlayerUp[i][start] = !isPlayerUp[i][start];
                                break;
                            }else {
                                printError();
                            }
                        }
                        if(main == '士'|| main == '仕') {
                            if(Math.abs(start - end) == 1) {
                                map[i - 1][end] = map[i][start];
                                map[i][start] = '口';
                                isPlayerUp[i - 1][end] = isPlayerUp[i][start];
                                isPlayerUp[i][start] = !isPlayerUp[i][start];
                                break;
                            }else {
                                printError();
                            }
                        }
                        map[i - end][start] = map[i][start];
                        map[i][start] = '口';
                        isPlayerUp[i - end][start] = !isPlayerUp[i][start];
                        isPlayerUp[i][start] = isPlayerUp[i][start];
                        break;
                    }
                }
            }
        }
    }

    public static void debug() {
       // endGame = true;
    }
    public static void main(String[] args) throws IOException{
        init();
        while(!endGame) {
            printMap();
            run();
            changeRoll();
            debug();
        }
    }
}
