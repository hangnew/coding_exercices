/* 여름을 맞아 친구들과 여행을 간 구름이는 369 게임을 하게 됐다.
369 게임은 여러명이 둘러앉아서 숫자를 하나씩 돌아가며 말하다가 숫자에 3,6,9가 포함된 숫자가 되면 박수를 치는 게임이다.
(이 때, 해당 숫자에 3,6,9가 여러개이면 박수를 개수만큼 쳐야한다. 예를 들어 33, 36의 경우 박수를 두 번 쳐야 한다)
게임이 끝난 숫자 N이 주어졌을 때, N 이전까지 박수를 친 횟수를 구하여라. */

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
