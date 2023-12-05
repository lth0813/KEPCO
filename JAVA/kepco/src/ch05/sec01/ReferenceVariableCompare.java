package ch05.sec01;

import java.util.*;

public class ReferenceVariableCompare {
	public static void main(String[] args) {
//		List<String> list = new ArrayList<String>();
		int [] array1;
		int [] array2;
		int [] array3;
		
		array1 = new int [] {1,2,3};
		array2 = new int [] {1,2,3};
		array3 = array2;
		System.out.println(array1 == array2);
		
		int a1 = array1[0];
		int a2 = array2[0];
		
		System.out.println(a1 == a2);
		System.out.println(array1[0] == array2[0]);
		System.out.println(array2 == array3);
		
		array2[0] = 100;
		System.out.println(array2[0]);
		System.out.println(array3[0]);
		System.out.println(array2 == array3);
	}
}
