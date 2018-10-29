import java.io.FileOutputStream;
import java.io.IOException;
import java.io.OutputStream;
import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.InetAddress;
import java.nio.ByteBuffer;
import java.util.Scanner;


public class Client {

	public static void main(String[] args) throws IOException {
		
		DatagramSocket ds = new DatagramSocket();
		
		InetAddress destinationAddress = InetAddress.getLocalHost();

		System.out.println("Enter File Name");
		Scanner sc = new Scanner(System.in);
		String fileName = sc.next();

		byte[] fileNameBytes = fileName.getBytes("utf-8");
		DatagramPacket fileNamePacket = new DatagramPacket(fileNameBytes,fileNameBytes.length,destinationAddress,5000);
		ds.send(fileNamePacket);
		
		byte[] fileContent = new byte[65535];
		DatagramPacket fileContentPacket = new DatagramPacket(fileContent,fileContent.length);
		ds.receive(fileContentPacket);
		
		OutputStream os = new FileOutputStream(fileName);
		os.write(fileContent,0,fileContentPacket.getLength());
		System.out.println("File Received");
		os.close();
		
		sc.close();
		ds.close();
		
	}

}
