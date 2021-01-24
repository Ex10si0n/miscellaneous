package comp212.courselab.GUI;

import javax.swing.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class TestGUI {
    public static void main(String[] args) {
        // Initialization JFrame
        JFrame f = new JFrame("JFrame - Test");
        f.setSize(400, 300);
        f.setLocation(200, 200);;
        f.setLayout(null);

        final JLabel l = new JLabel("Hi", JLabel.CENTER);
        final int[] clickTimes = {0};
        l.setText("Hello World");
        l.setBounds(50, 50, 280, 40);
        l.setOpaque(true);
        f.add(l);


        JButton b = new JButton("Test Me");
        b.setBounds(50, 150, 280, 30);
        b.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                l.setText("Button on click " + clickTimes[0] + " times.");
                clickTimes[0]++;
                b.setText("Add one");
            }
        });
        f.add(b);

        // Initialization JDialog
        JDialog d = new JDialog();
        d.setTitle("Dialog");
        d.setSize(400, 300);
        d.setLocation(100, 100);
        d.setLayout(null);
        d.add(b);
        d.setVisible(true);

        f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        f.setVisible(true);
    }
}
