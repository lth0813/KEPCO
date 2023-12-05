package generic.kepco.com;

import java.util.TreeSet;
import java.util.Random;

public class TreeSetLotto {
	
	private Random rd = new Random();

	public void makeLotto() {
		TreeSet<Integer> ts = new TreeSet<>();
		ts.add((rd.nextInt(45)+1));
		while(ts.size()<6) {
			ts.add((rd.nextInt(45)+1));
		}
		
		System.out.println(ts);
	}
	
	public static void main(String[] args) {
		new TreeSetLotto().makeLotto();

	}

}
