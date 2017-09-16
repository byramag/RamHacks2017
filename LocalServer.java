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
	
	public void send() {
		
	}
	
	public String receive() {
		return "hello";
	}
}