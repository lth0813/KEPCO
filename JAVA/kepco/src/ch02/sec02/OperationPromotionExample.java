package ch02.sec02;

public class OperationPromotionExample {
	public static void main(String[] args) {
		byte result = 10+20;
		System.out.println(result);
		
		byte val1 = 10;
		byte val2 = 20;
		int result1 = val1 + val2;
		System.out.println(result1);
		
		byte val4 = 10;
		int val5 = 20;
		long val3 = 10000000000000L;
		float result2 = val4 + val5 + val3;
		double result3 = val4 + val5 + val3;
		System.out.println(val3);
		System.out.println(result2);
		System.out.println(result3);
	}
}
