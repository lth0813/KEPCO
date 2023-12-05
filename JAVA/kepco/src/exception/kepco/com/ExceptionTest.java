package exception.kepco.com;

public class ExceptionTest {
	
//	반드시 예외처리를 해야 하는 경우...하지 않으면 문법적으로 에러임
//	1. DB 접속
//	2. 네트워크
//	3. I/O..스트림
//	4. 쓰레드 사용
	public void test() {
		try {
		int result = 10/0;
		} catch(Exception e) {
			System.out.println("분모로 0이 오면 안돼요");
			e.printStackTrace();
			e.getMessage();
		} finally {
			System.out.println("예외가 발생하나 하지 않으나 수행됩니다");
		}
		
	}
	
	public void test1() throws Exception{
		int result = 10/0;
	}
	
	public void test2() {
		try {
			int result = 10/0;
		} catch (Exception e) {
			new KepcoException(e);
		}
	}

	public static void main(String[] args) {
		new ExceptionTest().test();
		
		System.out.println();
		
		try {
			new ExceptionTest().test1();	
		} catch(Exception e) {
			System.out.println("메인 메소드에서 예외처리");
			e.printStackTrace();
		}
		
		System.out.println();
		
		new ExceptionTest().test2();
		
	}

}
