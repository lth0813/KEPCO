package ch05.sec01;

public class GarbageObjectExample {
	public static void main(String[] args) {
//		String hobby = "여행";
//		hobby = null;
//		
//		String kind1 = "자동차";
//		String kind2 = kind1;
//		kind1 = null;
//		System.out.println("kind2 : "+kind2);
		String a = "abc";
		String b = "abc";
		String c = new String("abc");
		System.out.println(a+b+c);
		System.out.println(a.hashCode());
		System.out.println(b.hashCode());
		System.out.println(c.hashCode());
		System.out.println(a.equals(c));
		System.out.println(a == c.toString());
	}
}
