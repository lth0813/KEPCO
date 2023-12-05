package generic.kepco.com;

public class ArrayTest {
	public void test() {
//		1차원 배열 선언
		int[] full = {1,3,5,7};
//		int full2[] = {1,3,5,7};
//		int[] full = new int[4];
//		int[] full = new int[] {1,3,5,7};
		
//		2차원 배열 선언
//		int[][] full = new int[5][5];
//		int[][] full = {{},{},{},{},{}};
		
//		2차원 배열의 크기가 다를 경우
//		int[][] diff = new int[3][];
//		diff[0] = new int[2];
//		diff[1] = new int[3];
//		diff[2] = new int[4];
		
		for (int i = 0; i < full.length; i++) {
			System.out.print(full[i]+" ");
		}
		System.out.println();
		System.out.println("*****************");
		for(int temp:full) {
			System.out.print(temp+" ");
		}
		System.out.println();
		System.out.println("*****************");
		int value=1;
		int[][] human = new int[5][5];
		for (int i = 0; i < human.length; i++) {
			for (int j = 0; j < human[i].length; j++) {
				human[i][j] = value;
				value++;
			}
		}
		
		for(int[] temp:human) {
			for(int present:temp) {
				System.out.print(present+" ");
			}
		}
		
	}

	public static void main(String[] args) {
		new ArrayTest().test();
	}

}
