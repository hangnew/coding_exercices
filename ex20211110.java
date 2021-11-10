// NxN 격자 모양의 공터에서 KxK 정사각형 크기의 땅을 구매하려고 할 때,
// 구매할 땅에 포함 된 폐기물의 수를 최소로 할 수 있는 영역을 찾을 수 있는 프로그램을 작성해보자

// 첫 줄에는 테스트케이스의 수를 나타내는 1 이상 100 이하의 자연수 T가 주어진다.
// 각 테스트케이스의 첫 줄에는 두 자연수 공터의 크기를 나타내는 N과 구매할 땅의 크기를 나타내는 K가 주어진다.
// 이후 N줄에 걸쳐서 공터의 각 행의 정보가 차례로 주어진다. 
// (0은 비어있는 땅을 나타내며, 1은 폐기물이 존재하는 칸을 나타낸다)

// 각 테스트케이스에 대하여 KxK 모양의 땅을 구매했을 때 얻을 수 있는 최소의 폐기물의 수를 공백없이 한 줄에 출력한다.


import java.io.*;
import java.lang.*;
import java.util.*;


public class Main {
	public static final Scanner scanner = new Scanner(System.in);
	
	public static void testCase(int caseIndex) {
		int N = scanner.nextInt();  // 지도의 크기 
		int K = scanner.nextInt();  // 놀이공원의 크기
		
		int[][] wastes = new int[N][N]; // 각 칸의 쓰레기 존재 여부 
		for (int r = 0; r < N; r += 1) {
			for (int c = 0; c < N; c += 1) {
				wastes[r][c] = scanner.nextInt();
			}
		}
		
		int loop = N - K + 1;
		int min = K * K;
		
		for (int y = 0; y < loop; y++) {
			for (int x = 0; x < loop; x++) {
				int tempMin = 0;
				int az = y + K;
				for (int a = y; a < az; a++) {
					int bz = x + K;
					for (int b = x; b < bz; b++) {
						tempMin = (wastes[a][b] == 1) ? tempMin + 1 : tempMin;
					}
				}
				min = (tempMin < min) ? tempMin : min;
			}
		}
		System.out.println(min);
	}
	
	public static void main(String[] args) throws Exception {
		int caseSize = scanner.nextInt();
		
		for (int caseIndex = 1; caseIndex <= caseSize; caseIndex += 1) {
			testCase(caseIndex);
		}
		
	}
	
}
