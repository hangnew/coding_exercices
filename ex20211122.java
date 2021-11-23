// 첫 줄에 램프의 세로 길이 n과 가로 길이 m이 입력된다.
// 다음에는 n*m의 램프가 입력되며, 켜진 램프는 1, 꺼진 램프는 0으로 입력된다.
// 다음 줄에는 프로그래밍 하는 수(p)가 입력된다.
// 그 다음으로는 p개의 줄로, 가로는 0, 세로는 1과, 프로그래밍을 하는 줄이 입력된다.
// 단, 프로그래밍 하는 줄이 가로인 경우 n보다 작고, 세로인 경우 m보다 작다.


// 5, 8 runtime error

import java.util.*;
class Main {
	public static void main(String[] args) throws Exception {
		Scanner sc = new Scanner(System.in);
		boolean[][] bulbs = new boolean[sc.nextInt()][sc.nextInt()];
		for (int i = 0; i < bulbs.length; i++) {
			for (int j = 0; j < bulbs[i].length; j++) {
				bulbs[i][j] = (sc.nextInt() == 1);
			}
		}
		int p = sc.nextInt();
		for (int i = 0; i < p; i++) {
			int rowCol = sc.nextInt(); // row, column (0, 1)
			int line = sc.nextInt() - 1;
			if (rowCol == 0) { // 가로
				for (int j = 0; j < bulbs[line].length; j++) {
					bulbs[line][j] = !bulbs[line][j];
				}
			} else { // 세로
				for (int j = 0; j < bulbs.length; j++) {
					bulbs[j][line] = !bulbs[j][line];
				}
			}
		}
		sc.close();
		for (int i = 0; i < bulbs.length; i++) {
			for (boolean bool : bulbs[i]) {
				int result = (bool) ? 1 : 0;
				System.out.print(result + " ");
			}
			System.out.println();
		}
	}
}
