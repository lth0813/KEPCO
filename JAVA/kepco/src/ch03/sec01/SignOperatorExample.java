package ch03.sec01;

public class SignOperatorExample {
	public static void main(String[] args) {
		int x = -100;
		x = -x;
		System.out.println(x);
		
		byte b = 100;
		int y = -b;
		System.out.println(y);
		y++;
		System.out.println(y);
		int i = 0;
		for (i = 0; i < 150; i++) {
			++y;
		}
		System.out.println(y);
		System.out.println(i);
		
		for (i = 0; i < 150; i++) {
			--y;
		}
		System.out.println(y);
		
		for (i = 0; i < 300; i++) {
			++b;
		}
		System.out.println(b);
//		b는 바이트 범위 때문에 양수와 음수를 왔다갔다함
	}
}
