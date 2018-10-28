
import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.OutputStream;
import java.net.Socket;
import java.net.UnknownHostException;
import java.util.Scanner;

public class Client {
	
	static void fileTransfer(DataInputStream dis, DataOutputStream dos) throws IOException
	{
		Scanner sc = new Scanner(System.in);
		System.out.print("Enter Name of File to receive : ");
		String fileName = sc.next();
		dos.writeUTF(fileName);
		int len = dis.readInt();
		byte[] contents = new byte[len];
		dis.read(contents);
		OutputStream os = new FileOutputStream(fileName);
		os.write(contents);
		System.out.println("File Received");
		os.close();
	}
	
	static void calculator(DataInputStream dis, DataOutputStream dos) throws IOException
	{
		Scanner sc = new Scanner(System.in);
		System.out.println("Enter choice \n1: addition\n2: substraction\n3: multiplication\n4: division");
		int choice = sc.nextInt();

		System.out.print("Enter 1st number : ");
		float first = sc.nextFloat();
		System.out.print("Enter 2nd number : ");
		float second = sc.nextFloat();
		dos.writeInt(choice);
		dos.writeFloat(first);
		dos.writeFloat(second);
		Float result = dis.readFloat();
		System.out.println("Result : "  + result.toString());
	}

	@SuppressWarnings("unused")
	public static void main(String[] args) throws UnknownHostException, IOException {
		Socket s = new Socket("127.0.0.1",5000);
		
		DataInputStream dis = new DataInputStream(s.getInputStream());
		DataOutputStream dos = new DataOutputStream(s.getOutputStream());

		Scanner sc = new Scanner(System.in);
		System.out.println("Enter choice : \n1: Echo Message\n2: File Transfer\n3: Calculator");
		int choice = sc.nextInt();
		dos.writeInt(choice);
		switch(choice) 
		{
			case 1:
				System.out.println("Enter Message");
				String str = sc.next();
				dos.writeUTF(str);
				System.out.println("Received message : " + dis.readUTF());
				break;
			case 2:
				fileTransfer(dis,dos);
				break;
			case 3:
				calculator(dis,dos);
				break;
		}
		
	}

}
