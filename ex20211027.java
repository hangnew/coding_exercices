import java.util.*;

class Main {
	public static void main(String[] args) throws Exception {
		Scanner sc = new Scanner(System.in);
		final int N = sc.nextInt();
		int sum = 0;
		for (int i = 1; i <= N; i++) {
			String temp = String.valueOf(i);
			if (temp.contains("3") || temp.contains("6") || temp.contains("9")) {
				sum++;
			}
		}
		System.out.println(sum);
		sc.close();
	}
}
