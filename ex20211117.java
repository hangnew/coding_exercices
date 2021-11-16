// 정렬된 배열 A, B가 주어지면 배열을 합친 후 다시 정렬하는 프로그램을 작성하십시오.
// 1. 첫 번째 줄에 배열 A, B의 크기 순서대로 입력
// 2. 다음 줄에 배열 A의 내용, 그 다음 줄에 배열 B의 내용 입력
// 3. 두 배열을 합친 결과를 출력한다.

import java.util.*;
class Main {
	public static void main(String[] args) throws Exception {
		Scanner sc = new Scanner(System.in);
		int a = sc.nextInt();
		int b = sc.nextInt();
		int l = a + b;
		int[] arr = new int[l];
		for (int i = 0; i < l; i++) {
			arr[i] = sc.nextInt();
		}
		sc.close();
		for (int i = 1; i < l; i++) {
			for (int j = 0; j < l - 1; j++) {
				if (arr[j] > arr[j + 1]) {
					int t = arr[j];
					arr[j] = arr[j + 1];
					arr[j + 1] = t;
				}
			}
		}
		for (int n : arr) {
			System.out.print(n + " ");
		}
	}
}
