package generic.kepco.com;

public class Mabang {
	
	int num;
	
	public Mabang(int num) {
		this.num=num;
	}
	public Mabang() {
		
	}
	
	public void makeMabang() {
		int[][] mabang = new int[num][num];
		int x = 0;
		int y = num/2;
		mabang[x][y] = 1;
		for (int i = 2; i <= num*num; i++) {
			x--;
			y--;
//		내 풀이
//			if(x < 0 & y < 0) {
//				x = x + 2;
//				y = y + 1;
//				mabang[x][y] = i;
//			} else if(x < 0) {
//				x = x+num;
//				mabang[x][y] = i;
//			} else if(y < 0) {
//				y = y+num;
//				mabang[x][y] = i;
//			} else if(mabang[x][y] != 0) {
//				x = x + 2;
//				y = y + 1;
//				if(x > num) {
//					x = 0;
//					mabang[x][y] = i;
//				} else {
//					mabang[x][y] = i;
//				}
//			} else {
//				mabang[x][y] = i;
//			}		
//		}
//			
//		교수님 풀이
			if(x<0) {
				if(y<0) {
					x=x+2;
					y=y+1;
				} else {
					x=x+num;
				}
			} else {
				if(y<0) {
					y=y+num;
				} else {
					if(mabang[x][y]!=0) {
						x=x+2;
						y=y+1;
					}
				}
			}
			mabang[x][y]=i;
		}	
		
//		출력용 for 문
//		for (int i = 0; i < mabang.length; i++) {
//			for (int j = 0; j < mabang[i].length; j++) {
//				System.out.print(mabang[i][j]+" ");	
//			}
//			System.out.println();	
//		}
		
//		출력용 향상된 for 문
		for (int[] temp:mabang) {
			for (int value:temp) {
				System.out.print(value+" ");
			}
			System.out.println();
		}
	}

	public static void main(String[] args) {
		new Mabang(5).makeMabang();

	}

}
