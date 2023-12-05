package generic.kepco.com;

import java.util.Random;

public class Lotto {
	private Random rd;
	private int[] lotto = new int[6];
	
	public void makeLotto() {
		rd = new Random();
		lotto[0] = rd.nextInt(45)+1;
		for(int i=1; i<6; i++) {
			int temp = rd.nextInt(45)+1;
			lotto[i]=temp;
			
//			결과는 나오지만 필요없는 for문이 돌고 있음
//			for (int j = 0; j < i; j++) {
//				if(lotto[j]==temp) {
//					i--;
//				}
//			}
			for (int j = 0; j < i; j++) {
				if(lotto[j]==temp) {
					i--;
					break;
				}
			}
			
		}	
		for (int i = 0; i < lotto.length; i++) {
			System.out.print(lotto[i]+" ");
		}
	}
	public static void main(String[] args) {
		new Lotto().makeLotto();

	}

}
