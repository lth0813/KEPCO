package generic.kepco.com;

public class StringTest {
	
	public void test() {
		String a = "test";
		String b = "test";
		String c=a;
		String d = new String("test");
//		Object 클래스에 선언되어 있는 equals()는 ==과 같음 (참조값을 비교함)
//		String 클래스의 equals()는 오버라이딩 되어서 문자열 내용 비교
		System.out.println(a);
		System.out.println(a.equals(c));
		System.out.println(a.equals(b));
		System.out.println(a.equals(d));
		System.out.println(a==d);
		System.out.println(a==b);
		System.out.println(a==c);
		
//		StringBuffer sb = new StringBuffer(); 동기화 기능이 있음
		StringBuilder sb = new StringBuilder("Select * ");
		sb.append(" from emp ");
		sb.append(" where... ");
		
		
	}

	public static void main(String[] args) {
		new StringTest().test();

	}

}
