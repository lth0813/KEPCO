package ch02.sec02;

public class VariableScopeExample {
	public static void main(String[] args) {
		int v1 = 15;
		int v2 = 0;
		if (v1 < 10) {
			v2 = v1 - 10;
//			System.out.println(v2);
		}
		System.out.println(v2);
	}	
}
