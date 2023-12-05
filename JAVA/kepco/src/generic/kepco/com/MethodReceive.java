package generic.kepco.com;

public class MethodReceive {

	public void receive(Elec elec) {
		System.out.println(elec+"receive 쪽입니다");
		MP3 mp3 =(MP3)elec;
		mp3.temp=999999;
	}
	
	public int receive1() {
		return 777777;
	}
	
	public int receive2(int first, int second) {
		return first + second;
	}
	
	public Elec receive3() {
		return new TV();
	}
}
