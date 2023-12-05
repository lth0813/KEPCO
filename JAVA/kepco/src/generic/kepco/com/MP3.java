package generic.kepco.com;

public class MP3 implements Elec{
	int temp = 3;
	@Override
	public void volumeUp() {
		System.out.println("MP3 볼륨업");
		
	}

	@Override
	public void volumeDown() {
		System.out.println("MP3 볼륨다운");
		
	}
	

}
