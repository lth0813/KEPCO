package network.kepco.com;

import java.io.BufferedReader;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.Socket;

public class Client {
	BufferedReader br;
	PrintWriter pw;
	Socket client;
	
	public Client() throws Exception{
		connect();
	}
	
	public void connect() throws Exception {
		System.out.println("서버로 접속을 시도 합니다");
		client = new Socket("10.10.21.89", 23333);
		System.out.println("접속 성공!!!");
		
		BufferedReader br = new BufferedReader(new InputStreamReader(client.getInputStream()));
		
		PrintWriter pw = new PrintWriter(client.getOutputStream(),true);
		pw.println("처음입니다 잘 모르니 잘 지도 부탁드립니다");
		
//		System.out.println(br.readLine());
		
		br.close();
//		pw.close();
	}

	public static void main(String[] args) throws Exception {
		new Client();

	}

}
