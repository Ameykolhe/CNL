
import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStream;
import java.net.ServerSocket;
import java.net.Socket;

public class Server {
	
	static void fileTransfer(DataInputStream dis, DataOutputStream dos) throws IOException
	{
		String fileName = dis.readUTF();
		InputStream is = new FileInputStream(fileName);
		int len = (int) new File(fileName).length();
		byte[] contents = new byte[len];
		is.read(contents);
		dos.writeInt(len);
		dos.write(contents);
		is.close();
	}
	
	static void calculator(DataInputStream dis, DataOutputStream dos) throws IOException
	{
		int choice = dis.readInt();
		float first = dis.readFloat();
		float second = dis.readFloat();
		float result = 0.0f;
		switch(choice)
		{
			case 1:
				result = first + second;
				break;
			case 2:
				result = first - second;
				break;
			case 3:
				result = first * second;
				break;
			case 4:
				result = first / second;
				break;
		}

		dos.writeFloat(result);
	}

	@SuppressWarnings("unused")
	public static void main(String[] args) throws IOException {
		ServerSocket ss = new ServerSocket(5000);
		Socket s = ss.accept();
		System.out.println("New Connection Received : " + s.getLocalAddress().toString());
		DataInputStream dis = new DataInputStream(s.getInputStream());
		DataOutputStream dos = new DataOutputStream(s.getOutputStream());
		
		int choice = dis.readInt();
		
		switch(choice) 
		{
			case 1:
				dos.writeUTF(dis.readUTF());
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
