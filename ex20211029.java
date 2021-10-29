// 이 문제는 반복문을 실습할 수 있는 피라미드 쌓기입니다. 입력한 수가 피라미드의 층수가 된다고 생각하고 '*'로 이루어진 피라미드 모양을 출력하는 프로그램을 작성하십시오.
  
import java.util.*;
class Main {
	public static void main(String[] args) throws Exception {
		Scanner sc = new Scanner(System.in);
		int row = sc.nextInt();
		for (int i = 0; i < row; i++) {
			for (int j = 0; j < row - 1 - i; j++) {
				System.out.print(" ");
			}
			for (int k = 0; k < 2 * i + 1; k++) {
				System.out.print("*");
			}
			System.out.println();
		}
		sc.close();
	}
}
