package ch03.sec01;

public class IfNestedExample {
	public static void main(String[] args) {
		int score;
		char grade = 'D';
		score = (int)(Math.random()*100);
		
		//90 이상이면 A, 80 이상 B, 70 이상 C, 나머지 D
		if (score >= 90) {
			grade = 'A';
		} else {
			if (score >= 80) {
				grade = 'B';
			} else {
				if (score >= 70) {
					grade = 'C';
				} 
			}
		}
		System.out.println("Score : "+score+" / Grade : "+grade);
	}
}
