package studio.aspire.jdbc;

import java.sql.*;

public class TestJDBC {
    public static void init(Connection c) throws SQLException {
        Statement s = c.createStatement();
        // String sql = "CREATE TABLE EMPLOYEE(ID INT, NAME VARCHAR(20), AGE INT, EMAIL VARCHAR(30);";
        String sql = "INSERT INTO EMPLOYEE VALUES(2, 'Steve', 19, 'me@aspire.studio');";
        s.execute(sql);
    }

    public static void add100(Connection c) throws SQLException {
        Statement s = c.createStatement();
        String sql;
        int cur_num;
        for (int i = 0; i < 100; i++) {
            cur_num = i + 3;
            sql = "INSERT INTO EMPLOYEE VALUES("+cur_num+", 'Employee"+cur_num+"', 23, 'e"+cur_num+"@employee.email');";
            s.execute(sql);
        }
    }

    public static void del100(Connection c) throws SQLException {
        Statement s = c.createStatement();
        String sql;
        sql = "DELETE FROM EMPLOYEE WHERE NAME LIKE 'E%';";
        s.execute(sql);
    }

    public static void upd100(Connection c) throws SQLException {
        Statement s = c.createStatement();
        String sql;
        for (int i = 0; i < 100; i++) {
            sql = "UPDATE EMPLOYEE SET NAME = 'E"+i+"' WHERE ID = "+(i+3)+";";
            s.execute(sql);
        }
    }

    public static void query(Connection c) throws SQLException {
        Statement s = c.createStatement();
        String sql;
        sql = "SELECT * FROM EMPLOYEE";
        ResultSet rs = s.executeQuery(sql);
        while(rs.next()) {
            int id = rs.getInt("id");
            String name = rs.getString(2);
            int age = rs.getInt("age");
            String email = rs.getString(4);
            System.out.printf("%d\t%s\t%d\t%s\n", id, name, age, email);
        }

    }

    public static void main(String[] args) {
        Connection c = null;
        Statement s = null;
        try {
            Class.forName("com.mysql.cj.jdbc.Driver");
            c = DriverManager.getConnection("jdbc:mysql://127.0.0.1:3306/java_conn_learn", "root", "");
            System.out.println("数据库加载成功");
            System.out.println("连接成功，获取连接对象: " + c);
            s = c.createStatement();
            System.out.println("获取 Statement 对象: " + s);
            // init(c);
            // add100(c);
            del100(c);
            // upd100(c);
            query(c);
        } catch (SQLException e) {
            e.printStackTrace();
        } catch (ClassNotFoundException e) {
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
}
