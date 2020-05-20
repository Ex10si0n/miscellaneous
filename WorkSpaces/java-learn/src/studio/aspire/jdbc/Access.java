package studio.aspire.jdbc;

import java.sql.*;
import java.util.Scanner;

public class Access {
    private static void operate(Connection c, String name, String pw) throws SQLException {
        Statement s = c.createStatement();
        while (true) {
            Scanner scanner = new Scanner(System.in);
            System.out.print(name+" > ");
            String instr = scanner.nextLine();
            if (instr.equals("logout")) {
                break;
            }
            if (instr.equals("showinfo")) {
                String sql = "SELECT * FROM ACCOUNT WHERE USRNAME='"+name+"' AND PASSWORD='"+pw+"';";
                ResultSet rs = s.executeQuery(sql);
                while(rs.next()) {
                    int id = rs.getInt("id");
                    String usrName = rs.getString(2);
                    String passWord = rs.getString(3);
                    String authority = rs.getString(4);
                    String pwstring = "";
                    for (int i = 0; i < passWord.length(); i++) pwstring=pwstring+"*";
                    System.out.println("| UID: U"+id+" | User Name: "+name+" | Password: "+pwstring+" | Authority: "+authority+" |");
                }
            }
            if (instr.equals("root")) {
                System.out.print("输入root密码获取权限 > ");
                String code = scanner.nextLine();
                if(code.equals("admin")) {
                    System.out.println("管理员权限已更新");
                    s.execute("UPDATE ACCOUNT SET AUTHORITY = 'Admin' WHERE USRNAME='"+name+"';");
                } else {                    System.out.println("密码错误")
;
                }
            }
            if (instr.equals("showallusrs")) {
                String sql = "SELECT * FROM ACCOUNT WHERE USRNAME='"+name+"' AND PASSWORD='"+pw+"';";
                ResultSet rs = s.executeQuery(sql);
                String usrName = null;
                while(rs.next()) {
                    usrName = rs.getString(2);
                }
                sql = "SELECT * FROM ACCOUNT WHERE USRNAME='"+usrName+"' AND PASSWORD='"+pw+"';";
                String authority = null;
                rs = s.executeQuery(sql);
                while(rs.next()) {
                    authority = rs.getString(4);
                }
                if (authority.equals("Admin")) {
                    sql = "SELECT * FROM ACCOUNT";
                    rs = s.executeQuery(sql);
                    while(rs.next()) {
                        int id = rs.getInt("id");
                        usrName = rs.getString(2);
                        String passWord = rs.getString(3);
                        authority = rs.getString(4);
                        System.out.println("| UID: U"+id+" | User Name: "+usrName+" | Password: "+passWord+" | Authority: "+authority+" |");
                    }
                }else {
                    System.out.println("权限不足，操作被禁止");
                }
            }
        }
    }

    public static void signUp(Connection c) throws SQLException {
        Scanner scanner = new Scanner(System.in);
        System.out.print("输入用户名：");
        String usrName = scanner.nextLine();
        System.out.print("输入密码：");
        String passWord = scanner.nextLine();
        System.out.print("确认密码：");
        String checkPass = scanner.nextLine();
        while (!passWord.equals(checkPass)) {
            System.out.print("输入不正确，请再次确认密码：");
            checkPass = scanner.nextLine();
        }
        Statement s = c.createStatement();
        String sql = "INSERT INTO ACCOUNT(USRNAME, PASSWORD, AUTHORITY) VALUES('"+usrName+"', '"+passWord+"', 'User');";
        s.execute(sql);
        System.out.println("注册成功");
    }

    public static void logIn(Connection c) throws SQLException {
        Statement s = c.createStatement();
        Scanner scanner = new Scanner(System.in);
        System.out.print("用户名：");
        String usrName = scanner.nextLine();
        System.out.print("密码：");
        String passWord = scanner.nextLine();
        String sql = "SELECT * FROM ACCOUNT WHERE USRNAME='"+usrName+"' AND PASSWORD='"+passWord+"';";
        ResultSet rs = s.executeQuery(sql);
        if(rs.next()) {
            System.out.println("登录成功");
            operate(c, usrName, passWord);
        } else
            System.out.println("登录失败");
    }

    public static void main(String[] args) throws SQLException {
        // 连接数据库
        Connection c = null;
        Statement s = null;
        try {
            Class.forName("com.mysql.cj.jdbc.Driver");
            c = DriverManager.getConnection("jdbc:mysql://127.0.0.1:3306/java_conn_learn", "root", "");
            Scanner scanner = new Scanner(System.in);
            String instr;
            while (true) {
                System.out.print("Instruction > ");
                instr = scanner.nextLine();
                if (instr.equals("signup")) {
                    // 注册账户
                    signUp(c);
                }
                if (instr.equals("login")) {
                    // 登录账户
                    logIn(c);
                }
                // 退出系统
                if (instr.equals("exit") || instr.equals("quit")) {
                    break;
                }
                if (instr.equals("h") || instr.equals("help")) {
                    help();
                }
            }

        } catch (ClassNotFoundException | SQLException e) {
            e.printStackTrace();
        } finally {
            if (s != null) {
                try {
                    s.close();
                } catch (SQLException e) {
                    e.printStackTrace();
                }
            }
            if (c != null) {
                try {
                    c.close();
                } catch (SQLException e) {
                    e.printStackTrace();
                }
            }
        }
    }

    private static void help() {
        System.out.println("== When in the instruction interface ==\n    signup: for Sign Up an account\n    login: for Log In your account\n== When Signed In ==\n    showinfo: Show your account's info\n    showallusrs: Show all users' info\n    root: get Admin Authority password is 'admin'");
    }
}
