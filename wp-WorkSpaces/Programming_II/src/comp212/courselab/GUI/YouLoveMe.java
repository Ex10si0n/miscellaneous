package comp212.courselab.GUI;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.Random;

public class YouLoveMe {
    public static void main(String[] args) {
        // Initialize JFrame Window
        JFrame controlPanel = new JFrame("Do you Love me?");
        controlPanel.setSize(500, 400);
        controlPanel.setLocation(200, 200);
        controlPanel.setLayout(null);

        final JLabel showMessage = new JLabel("Do you love me?", JLabel.CENTER);
        showMessage.setBounds(150, 50, 200, 40);

        // Initialize JButtons
        JButton yes = new JButton("Yes");
        JButton no = new JButton("No");
        yes.setBounds(130, 300, 100, 30);
        no.setBounds(270, 300, 100, 30);

        Random randomGenerator = new Random();

        no.addMouseListener(new java.awt.event.MouseAdapter() {
            public void mouseEntered(java.awt.event.MouseEvent evt) {
                int randX = randomGenerator.nextInt(400);
                int randY = randomGenerator.nextInt(300);
                no.setBounds(randX, randY, 100, 30);
            }
        });




        controlPanel.add(showMessage);
        controlPanel.add(yes);
        controlPanel.add(no);
        controlPanel.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        controlPanel.setVisible(true);
    }
}
