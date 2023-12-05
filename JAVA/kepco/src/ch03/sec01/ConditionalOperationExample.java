package ch03.sec01;

public class ConditionalOperationExample {
	public static void main(String[] args) {
		int score = (int)(Math.random()*100);
		char grade;
		
//		grade = (score > 90) ? 'A' : (score > 80) ? 'B' : 'C';
		grade = (score > 90) ? 'A' : (score > 80) ? 'B' : (score > 70) ? 'C' : 'D'; 
		
//		if (score > 90) {
//			grade = 'A';
//		} else if (score > 80) {
//			grade = 'B';
//		} else {
//			grade = 'C';
//		}
		System.out.println("Score : "+score+" / Grade : "+grade);
		
		int value = 356;
		System.out.println(value - value % 100);
	
	}
}
