package ch03.sec01;

public class InfinityAndNaNCheckExample {
	public static void main(String[] args) {
		int x = 5;
		double y = 0.0;
		double z = x/y;
		double z1 = z+1;
		double z2 = z1/z;
		if (!Double.isInfinite(z2) && !Double.isNaN(z2)) {
			System.out.println("계산 가능, 결과는 "+(z2));
		} else {
			System.out.println("계산 불가능");
		}
		
		float a = 0.1f;
		float b = (float) (a * (float) 0.1);
		System.out.println(b);
		System.out.println(b == 0.01f);
		
		String str1 = "abc";
		String str2 = "abc";
		
		System.out.println(str1 == str2);
	}
}
