package comp212.courselab.GUI;

import javax.swing.*;
import javax.swing.border.Border;
import java.awt.*;

public class ManagementSystem {
    public static void main(String[] args) {
        JFrame systemPanel = new JFrame("John Doe Management System");
        systemPanel.setSize(800, 600);
        systemPanel.setLocation(200, 200);
        systemPanel.setLayout(new BorderLayout());

        Border blackline = BorderFactory.createLineBorder(Color.BLACK);

        JLabel explorer = new JLabel("Explorer", JLabel.CENTER);
        JLabel panel = new JLabel("Panel", JLabel.CENTER);
        JLabel info = new JLabel("Info", JLabel.CENTER);
        JLabel menu = new JLabel("Menu", JLabel.CENTER);
        JLabel footbar = new JLabel("Footbar", JLabel.CENTER);

        explorer.setBorder(blackline);
        panel.setBorder(blackline);
        info.setBorder(blackline);
        menu.setBorder(blackline);
        footbar.setBorder(blackline);

        systemPanel.add(explorer, BorderLayout.WEST);
        systemPanel.add(panel, BorderLayout.CENTER);
        systemPanel.add(info, BorderLayout.EAST);
        systemPanel.add(menu, BorderLayout.NORTH);
        systemPanel.add(footbar, BorderLayout.SOUTH);

        systemPanel.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        systemPanel.setVisible(true);
    }
}
