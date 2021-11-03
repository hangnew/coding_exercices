// 한 변의 길이가 N인 정사각형 모양의 격자판이 있다.
// 이 격자판의 각 격자는 길이가 1일 때, 이 격자판의 크고 작은 정사각형의 개수는 총 몇 개일까?

import java.util.*;

class Main {
	public static void main(String[] args) throws Exception {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		System.out.println(squares(n));
		sc.close();
	}
  
	public static long squares(int n) {
		long squares = 0L;
		for (int i = 1; i < n + 1; i ++) {
			squares += (long)(Math.pow(i, 2));
		}
		return squares;
	}
}
