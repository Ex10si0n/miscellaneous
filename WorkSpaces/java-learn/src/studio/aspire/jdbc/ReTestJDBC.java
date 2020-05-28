package studio.aspire.jdbc;

import java.sql.*;
import java.util.Scanner;

public class ReTestJDBC {
    public static void query(Connection c) throws SQLException {
        String sql = "select * from employee";
        Statement s = c.createStatement();
        ResultSet rs = s.executeQuery(sql);
        System.out.printf("id  Name            Age   Email\n");
        while (rs.next()) {
            int id = rs.getInt(1);
            String name = rs.getString(2);
            int age = rs.getInt(3);
            String email = rs.getString(4);
            System.out.printf("%-3d %-15s %-5d %-20s\n", id, name, age, email);
        }
    }
    public static void modify(Connection c) throws SQLException {
        Statement s = c.createStatement();
        Scanner scan = new Scanner(System.in);
        String sql = "insert into employee values(null, ?, ?, ?)";
        PreparedStatement ps = c.prepareStatement(sql);
        System.out.print("Name: ");
        ps.setString(1, scan.next());
        System.out.print("Age: ");
        ps.setInt(2, scan.nextInt());
        System.out.print("E-mail: ");
        ps.setString(3, scan.next());
        System.out.println();
        ps.execute();
    }
    public static void exec(Connection c) throws SQLException {
        Statement s = c.createStatement();
        modify(c);
        query(c);
    }
    public static void main(String[] args) {
        try {
            Class.forName("com.mysql.cj.jdbc.Driver");
            Connection c = DriverManager.getConnection(
                    "jdbc:mysql://127.0.0.1:3306/java_conn_learn?characterEncoding=UTF-8",
                    "root", ""
            );
            System.out.println("Connection Success");
            exec(c);
        } catch (ClassNotFoundException e) {
            e.printStackTrace();
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }
}
