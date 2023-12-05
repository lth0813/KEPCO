package generic.kepco.com;

public class MethodSend {
	
	public void send() {
		MP3 mp3 = new MP3();
		MethodReceive mr = new MethodReceive();
		mr.receive(mp3);
		int result = mr.receive1();
		int result2 = mr.receive2(7,9);
		Elec elec = mr.receive3();
		
		System.out.println(result);
		System.out.println(result2);
		elec.volumeUp();
		elec.volumeDown();
		
		System.out.println(mp3+"send 쪽입니다");
		System.out.println(mp3.temp);
	}

}
