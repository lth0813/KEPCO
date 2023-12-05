package inherit.kepco.com;

import javax.swing.JFrame;

public class DesignTest extends JFrame{
	
	public DesignTest(String title) {
		super(title);
	}
	
	public static void main(String[] args) {
		DesignTest dt = new DesignTest("이것은 생성자 연습");
		dt.setBounds(300, 300, 300, 300);
		dt.setVisible(true);
	}

}
