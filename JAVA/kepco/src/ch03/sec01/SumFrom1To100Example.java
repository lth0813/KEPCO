package ch03.sec01;

public class SumFrom1To100Example {
	public static void main(String[] args) {
		int sum = 0;
		int i = 0;
		for (i = 0;i <= 100; i++) {
			sum += i;
		}
		System.out.println("1 ~ "+(i-1)+" / 총합 : "+sum);
	}
}
