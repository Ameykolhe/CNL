import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStream;
import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.InetAddress;
import java.nio.ByteBuffer;

public class Server {

	public static void main(String[] args) throws IOException {
		
		DatagramSocket ds = new DatagramSocket(5000);

		byte[] fileNameBytes = new byte[256];
		DatagramPacket fileNamePacket = new DatagramPacket(fileNameBytes,fileNameBytes.length);
		ds.receive(fileNamePacket);
		String fileName = new String(fileNameBytes, 0, fileNamePacket.getLength(),  "utf-8");

		System.out.println('*' + fileName + '*');
		
		InputStream is = new FileInputStream(fileName);
		int len = (int) new File(fileName).length();
		byte[] contents = new byte[len];
		is.read(contents);
		in.close();
		
		InetAddress destinationAddress = InetAddress.getLocalHost();
		DatagramPacket contentPacket = new DatagramPacket(contents , contents.length , destinationAddress , fileNamePacket.getPort() );
		
		ds.send(contentPacket);
		System.out.println("File Sent");

		ds.close();
		
	}

}
