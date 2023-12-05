package dbconn.kepco.com;

import java.sql.Connection;
import java.sql.DriverManager;

public class DBconnSingleTon {
//	singleton 객체는 메모리에 1개만 인스턴스화 하여 사용하는 방법
//	그래서 이렇게 만들어야 함
//	1. 외부에서 new 해서 못만들도록 해야함 - 생성자를 private 만들어서 막는다.
	
	private static DBconnSingleTon dst = new DBconnSingleTon();
	Connection conn;
	
	private DBconnSingleTon(){
		try {
			conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/hr", "hr", "1234");
		} catch(Exception e) {
			e.printStackTrace();
		}
	}
	
	public static DBconnSingleTon getInstance() {
		if(dst==null) {
			dst = new DBconnSingleTon();
		}
		return dst;
	}
	
	public Connection getConnection() {
		return conn;
	}
	
}
