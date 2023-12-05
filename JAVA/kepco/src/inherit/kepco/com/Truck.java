package inherit.kepco.com;

public class Truck {
	private int speed;
	String color = "Red";
	public String money="free";
	// final이 변수 앞에 붙으면 상수가 된다. 이 때 변수명은 대문자로 적자
	final int TEST=100;
	// 두개 이상의 단어(연어)로 변수명을 선언하는 규칙
	String nickName="human";
	public String front(int speed) {
		this.speed=speed;
		// return을 만나면 해당 메소드는 종료
		return null;
	}
	public void rear() {
		System.out.println("후진 속도도 " +speed+"입니다");
	}
}
