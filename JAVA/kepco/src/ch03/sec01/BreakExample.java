package ch03.sec01;

public class BreakExample {
	public static void main(String[] args) {
		while (true) {
			int randomInteger = (int)(Math.random()*6)+1;
			System.out.println(randomInteger);
			if (randomInteger==6) {
				break;
			}
			System.out.println("if문 밖인가?");
		}
		System.out.println("while문 밖인가?");
	}
}
