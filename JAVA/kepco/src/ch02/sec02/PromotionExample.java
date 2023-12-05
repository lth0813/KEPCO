package ch02.sec02;

public class PromotionExample {
	public static void main(String[] args) {
		byte byteValue = 10;
		int intValue = byteValue;
		System.out.println("byteValue : "+byteValue);
		System.out.println("intValue : "+intValue);
		// 강제 타입 변환
		byte byteValue1 = 20;
		int intValue1 = (byte) byteValue1;
		System.out.println("byteValue1 : "+byteValue1);
		System.out.println("intValue1 : "+intValue1);
		
		
	}

}
