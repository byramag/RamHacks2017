public class backend {
	public static void main(String[] args) {
		LocalServer server = new LocalServer(1019);
		
		while (true) {
			server.receive();
		}
	}
}