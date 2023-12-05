package generic.kepco.com;

public class Radio implements Elec {

	@Override
	public void volumeUp() {
		System.out.println("Radio 볼륨업");
		
	}

	@Override
	public void volumeDown() {
		System.out.println("Radio 볼륨다운");
		
	}
	
	
}
