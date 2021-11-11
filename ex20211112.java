// 배열에 들어있는 정수 중 최소값을 구하는 프로그램을 작성하십시오.

import java.util.*;

class Main {
	public static void main(String[] args) throws Exception {
		Scanner sc = new Scanner(System.in);
		int[] arr = new int[sc.nextInt()];
		for (int i = 0; i < arr.length; i++) {
			arr[i] = sc.nextInt();
		}
    sc.close();
		Arrays.sort(arr);
		System.out.println(arr[0]);
	}
}
