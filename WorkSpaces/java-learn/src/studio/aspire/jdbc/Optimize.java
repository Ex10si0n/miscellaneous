package studio.aspire.jdbc;

import javax.xml.stream.events.StartDocument;
import java.sql.*;

public class Optimize {
    public static void main(String[] args) {

        try {
            Class.forName("com.mysql.cj.jdbc.Driver");
        } catch (ClassNotFoundException e) {
            e.printStackTrace();
        }
        // 使用 PreparedStatement 进行插入操作
        String sql = "INSERT INTO EMPLOYEE VALUES(NULL, ?, ?, ?);";
        try(Connection c = DriverManager.getConnection("jdbc:mysql://127.0.0.1:3306/java_conn_learn", "root", "");
            Statement s = c.createStatement();
            PreparedStatement ps = c.prepareStatement(sql);) {
            for(int i = 0; i < 10000; i++) {
                ps.setString(1, "employee"+i);
                ps.setInt(2, 24);
                ps.setString(3, "email@email.com");
                ps.execute();
            }
        } catch (SQLException throwables) {
            throwables.printStackTrace();
        }


    }
}
