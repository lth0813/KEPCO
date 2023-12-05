package ch03.sec01;

public class PrintFrom1To10Example {
	public static void main(String[] args) {
		int result = 0;
		for (int i = 1;i <= 10;i++) {
			System.out.println(i);
			result += i;
		}
		System.out.println(result);
	}
}
