import java.net.*;
import java.io.*;

public class LocalServer {
	private ServerSocket server;
	private Socket sock;
	
	public LocalServer(int port) {
		try {
			server = new ServerSocket(port, 1, InetAddress.getByName(null));
			sock = server.accept();
		} catch (Exception e) {
			System.out.println("Error occurred setting up server socket.");
		}
	}
	
	public void send(String message) {
		try {
			OutputStream sender = sock.getOutputStream();
			byte[] buffer = message.getBytes("US-ASCII");
			sender.write(buffer);
		} catch (IOException ioe) {
			System.out.println("Could not send message.");
		}
	}
	
	public String receive() {
		try {
			InputStream receiver = sock.getInputStream();
			byte[] buffer = new byte[receiver.available()];
			int bytecount = receiver.read(buffer);
			String message = new String(buffer, "US-ASCII");
			
			if (bytecount > 0)
				return message;
			else
				return null;
		} catch (IOException ioe) {
			System.out.println("Could not receive message.");
		}
		
		return null;
	}
}