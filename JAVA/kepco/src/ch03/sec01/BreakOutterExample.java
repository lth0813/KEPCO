package ch03.sec01;

public class BreakOutterExample {
	public static void main(String[] args) {
		int sum = 0;
		Outter: for(char upper='A'; upper<='Z'; upper++) {
			for(char lower='a'; lower<='z'; lower++) {
				sum++;
				if (lower == 'g') {
					break Outter;
				}
			}
			System.out.println("여긴가?");
		}
		System.out.println("아니면 여긴가?");
	}
}
