package stream.kepco.com;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.FileReader;
import java.io.FileWriter;

public class StreamTest {
	int temp;
	FileInputStream fi;
	FileOutputStream fo;
	
	public void test() {
		try {
		fi = new FileInputStream("c:/kepco_human/a.txt");
		fo = new FileOutputStream("c:/kepco_human/b.txt");	
		while((temp = fi.read()) != -1) {
				fo.write((char)temp);
			}
		} catch (Exception e) {
			e.printStackTrace();
		} finally {
			try {
			fi.close();
			fo.close();
			} catch (Exception e) {
				e.printStackTrace();
			}
		}
	}
	
	public void test1() {
//		1.8버전까지는 아래와 같이 사용해야 함
		try (FileReader fr = new FileReader("c:/kepco_human/a.txt");
			 FileWriter fw = new FileWriter("c:/kepco_human/c.txt")) {
			while((temp = fr.read()) != -1) {
				fw.write((char)temp);
			}
		} catch (Exception e) {
			e.printStackTrace();
		} 
	}
	public void test2() throws Exception {
//		1.9버전 이후 부터는 아래와 같이 사용 가능
		FileReader fr = new FileReader("c:/kepco_human/a.txt");
		FileWriter fw = new FileWriter("c:/kepco_human/d.txt");
		try (fr;fw) {
			while((temp = fr.read()) != -1) {
				System.out.print((char)temp);
				fw.write((char)temp);
			}
		} catch (Exception e) {
			e.printStackTrace();
		} 
	}
	public void test3() throws Exception {
		String temp=null;
		long start = System.currentTimeMillis();
		BufferedReader br = new BufferedReader(new FileReader("c:/kepco_human/a.txt"));
		BufferedWriter bw = new BufferedWriter(new FileWriter("c:/kepco_human/e.txt"));
		try (br;bw) {
			while((temp=br.readLine())!=null) {
				bw.write(temp);
				bw.write("/n");
			}
		} catch (Exception e) {
			e.printStackTrace();
		}
		long end = System.currentTimeMillis()-start;
		System.out.println("메소드 실행 시간은 "+ end + " 입니다.");
	}
		
	public static void main(String[] args) throws Exception {
//		new StreamTest().test();
//		new StreamTest().test1();
//		new StreamTest().test2();
		new StreamTest().test3();

	}

}
