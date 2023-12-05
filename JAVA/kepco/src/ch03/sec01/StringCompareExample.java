package ch03.sec01;

public class StringCompareExample {
	private String name;
	
	public StringCompareExample(String name) {
		this.name = name;
	}
	
	public static void main(String[] args) {
		StringCompareExample name1 = new StringCompareExample("thlim");
		StringCompareExample name2 = new StringCompareExample("thlim");
		
		System.out.println(name1.name);
		System.out.println(name2.name);
		
		String result1 = name1.name;
		String result2 = name2.name;
		
		System.out.println(name1.name == name2.name);
		System.out.println(result1.equals(result2));
		
		// &&, &, ||, |
	}
	
	
}
