public class backend {
	public static void main(String[] args) {
		LocalServer server = new LocalServer(23);
		
		while (true) {
			String message = server.receive();
			if (message != null)
				System.out.println(message);
		}
	}
}