package dbconn.kepco.com;

import java.sql.Timestamp;

public class EmployeeDTO {
	private int employeeId;
	private String firstName;
	private String email;
	private Timestamp hireDate;
	
	public int getEmployeeId() {
		return employeeId;
	}
	public void setEmployeeId(int employeeId) {
		this.employeeId = employeeId;
	}
	public String getFirstName() {
		return firstName;
	}
	public void setFirstName(String firstName) {
		this.firstName = firstName;
	}
	public String getEmail() {
		return email;
	}
	public void setEmail(String email) {
		this.email = email;
	}
	public Timestamp getHireDate() {
		return hireDate;
	}
	public void setHireDate(Timestamp hireDate) {
		this.hireDate = hireDate;
	}
	@Override
	public String toString() {
		return "EmployeeDTO [employeeId=" + employeeId + ", firstName=" + firstName + ", email=" + email + ", hireDate="
				+ hireDate + "]";
	}
	
	
	
}
