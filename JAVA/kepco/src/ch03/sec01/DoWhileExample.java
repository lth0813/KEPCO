package ch03.sec01;

import java.util.Scanner;

public class DoWhileExample {
	public static void main(String[] args) {
		System.out.println("메시지를 입력하세요");
		System.out.println("프로그램을 종료하려면 q를 입력하세요");
		String inputStr;
		do {
			System.out.print(">");
			Scanner scanner = new Scanner(System.in);
			inputStr = scanner.nextLine();
			System.out.println(inputStr);
		} while (!inputStr.equals("q"));
		
		System.out.println();
		System.out.println("프로그램 종료");
	}
}
			
	
