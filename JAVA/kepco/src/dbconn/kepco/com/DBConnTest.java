package dbconn.kepco.com;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;

public class DBConnTest {
	private Connection conn;
	private PreparedStatement pstm;
	private ResultSet rs;
	
	public void select() throws Exception {
		conn = DBconnSingleTon.getInstance().getConnection();
		String query = "SELECT EMPLOYEE_ID, FIRST_NAME, EMAIL, HIRE_DATE FROM EMPLOYEES";
		pstm = conn.prepareStatement(query);
//		1. 실행하는 쿼리문이 select문일 경우 executeQuery()
//		2. insert, update, delete일 경우는 executeUpdate()
		rs = pstm.executeQuery();
		
		while(rs.next()) {
			int employeeId = rs.getInt("employee_id");
			String firstName = rs.getString("first_name");
			String email = rs.getString("email");
			String hireDate = rs.getString("hire_date");
			System.out.println(employeeId+" "+firstName+" "+email+" "+hireDate);
			System.out.println();
			
		}
	}
	
	public void insert() throws Exception {
		conn = DBconnSingleTon.getInstance().getConnection();
		StringBuilder sb = new StringBuilder();
		sb.append("INSERT INTO EMPLOYEES VALUES");
		sb.append("(301,'A','B','C','D',NOW(),'AD_VP',6000,NULL,110,30)");
		pstm = conn.prepareStatement(sb.toString());
		pstm.executeUpdate();
	}
	
	public static void main(String[] args) throws Exception {
		DBConnTest dt = new DBConnTest();
		dt.select();
		dt.insert();
	}

}
