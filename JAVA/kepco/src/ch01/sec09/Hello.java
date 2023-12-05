package ch01.sec09;

public class Hello {

	public static void main(String[] args) {
		System.out.println("Hello Java");
		
//		Hello hello;
//		hello = new Hello();
//		int result = hello.add(10,5);
		int result = add(10,5);
		System.out.println(result);

	}
	
	static int add(int a, int b) {
		
		return a + b;
	}

}
