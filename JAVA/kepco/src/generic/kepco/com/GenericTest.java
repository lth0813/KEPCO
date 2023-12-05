package generic.kepco.com;

import java.util.ArrayList;

public class GenericTest {
	ArrayList<Elec> human;
	public void test() {
		human = new ArrayList();
//		제네릭을 이용해서 Upcasting
		human.add(new MP3());
		human.add(new TV());
		human.add(new Radio());
//		익명클래스 활용
		human.add(new Elec(){
			@Override
			public void volumeUp() {
				System.out.println("cell업");
			}
			@Override
			public void volumeDown() {
				System.out.println("cell다운");
			}
		});
//		System.out.println(human.size());
//		Object 클래스에 있는 ToString() 메소드는 println()을 만나면 실행됨
//		System.out.println(human);
//		System.out.println(new MP3());
	}
	
	public void result() {
		for (int i = 0; i < human.size(); i++) {
			human.get(i).volumeUp();
			human.get(i).volumeDown();
		}
		System.out.println("----------------");
		
		int j=0;
		while(j<human.size()) {
			human.get(j).volumeUp();
			human.get(j).volumeDown();
			j++;
		}
		
		System.out.println("----------------");
		
		for(Elec temp : human) {
			temp.volumeUp();
			temp.volumeDown();
		}
	}

}

