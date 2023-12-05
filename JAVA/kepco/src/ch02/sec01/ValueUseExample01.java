package ch02.sec01;

public class ValueUseExample01 {
	public static void main(String[] args) {
		ValueUseExample val = new ValueUseExample();
		
		int hours = val.hour;
		int minutes = val.minute;
		int totalTime = hours*60 + minutes;
		System.out.println(totalTime);
	}
}
