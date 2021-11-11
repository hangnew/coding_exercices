// 집 주변에 위치한 N개의 매점에서 N-2개의 물건을 사야한다.
// 집에서 출발하여 (N-2)개의 매점에서 필요한 물건을 1개씩 구매하고자 할 때, 최소한 적은 거리를 이동해야 한다.

// 1. 첫째 줄에 매점의 개수를 나타내는 정수 N과 집의 위치를 나타내는 정수 x가 공백으로 구분되어 주어진다.
// 2. 둘째 줄에 매점의 위치 p1, p2, ... , pN가 공백으로 구분되어 주어진다
// 3. N-2개의 물품을 사기 위해 이동해야 하는 거리의 최소값을 출력한다.

import java.util.*;
class Main {
  
	public static void shortcut(int n, int x, int[] p) {
		int items = (n - 2 > 0) ? n - 2 : 0; // 사야할 물건 개수 (한 블럭당 매점 개수) 
		int loop = (n > 2) ? 3 : 0; // 반복할 횟수 
		
		// result = 첫 번째 블럭 최단거리 미리 구하기
		// 사야할 물건이 0인 경우 0
		int result = 0;
		if (items > 0) {
			int distance1 = Math.abs(p[items - 1] - p[0]);
			int fromFirst1 = Math.abs(p[0] - x);
			int fromLast1 = Math.abs(p[items - 1] - x);
			int startPoint1 = (fromFirst1 < fromLast1) ? fromFirst1 : fromLast1;
			result = distance1 + startPoint1;
		}
		
		// 두 번째 블럭부터 거리가 result보다 짧은지 비교
		for (int i = 1; i < loop; i++) {
			int distance = Math.abs(p[i + items - 1] - p[i]);
			int fromFirst = Math.abs(p[i] - x);
			int fromLast = Math.abs(p[i + items - 1] - x);
			int startPoint = (fromFirst < fromLast) ? fromFirst : fromLast;
			int tempResult = distance + startPoint;
			result = (tempResult < result) ? tempResult : result;
		}
		System.out.println(result);
	}
	
	
	public static void main(String[] args) throws Exception {
		Scanner sc = new Scanner(System.in);
		int numberOfShops = sc.nextInt(); // 매점 개수
		int myLocation = sc.nextInt(); // 재희 위치
		sc.nextLine();
		int[] shopsLocation = new int[numberOfShops];
		for (int i = 0; i < numberOfShops; i++) {
			shopsLocation[i] = sc.nextInt();
		}
		Arrays.sort(shopsLocation); // 오름차순 정렬
		
		shortcut(numberOfShops, myLocation, shopsLocation);
		
		sc.close();
	}
}
