1. 첫 줄에 배열의 숫자 개수
2. 다음 줄에 공백으로 구별하면서 배열에 수 입력
3. 합을 구하고자 하는 구간
4. 출력 : 구간의 합

import java.util.*;

class Main {
	public static void gimmesum(String[] arr, int n1, int n2) {
		int sum = 0;
		for (int i = n1; i < n2; i++) {
			sum += Integer.parseInt(arr[i]);
		}
		System.out.println(sum);
	}
	
	public static void main(String[] args) throws Exception {
		Scanner sc = new Scanner(System.in);
		sc.nextLine();
		String[] nums = sc.nextLine().split(" ");
		int first = sc.nextInt() - 1;
		int last = sc.nextInt();
		sc.close();
		gimmesum(nums, first, last);
	}
}
