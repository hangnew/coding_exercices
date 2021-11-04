// 유치원 정류장을 경유하는 버스가 N대 있고, 각 버스마다 그 날의 최초 운행 시각 s와 
// 정해진 루트를 돌고 다시 원위치로 오는 데 걸리는 시간 d가 있습니다.
// 소희의 엄마는 빨리 탈 수 있으면 어떤 버스든 상관없었기 때문에 정류장에 가장 먼저 도착하는 버스를 타려고 합니다.
// 각 버스는 1번부터 N번까지 번호가 매겨져 있고, 
// 만약 정류장에 가장 먼저 도착하는 버스가 여러 대라면 번호가 더 작은 버스를 탄다고 합니다.
// 소희와 소희의 엄마가 정류장에 도착한 시간이 T일 때, 소희와 소희의 엄마가 타게 될 버스는 몇 번인지 구해주세요.

import java.util.*;

class Main {
	public static int bus(int t, Map<Integer, int[]> map) {
		int key = 1;
		int term = 0;
		for (int i = 1; i < map.size() + 1; i++) {
			int busTime = map.get(i)[0];
			while (busTime + map.get(i)[1] <= t) {
				busTime += map.get(i)[1];
			}
			int tempTerm = (busTime > t) ? busTime - t : t - busTime;
			term = (i == 1) ? tempTerm : term;
			if (tempTerm < term) {
				term = tempTerm;
				key = i;
			}
		}
		return key;
	}
	
	public static void main(String[] args) throws Exception {
		Scanner sc = new Scanner(System.in);
		final int N = sc.nextInt();
		final int T = sc.nextInt();
		Map<Integer, int[]> sMap = new HashMap<>();
		for (int i = 0; i < N; i++) {
			int[] s = new int[2];
			s[0] = sc.nextInt();
			s[1] = sc.nextInt();
			sMap.put((i + 1), s);
		}
		sc.close();
		System.out.println(bus(T, sMap));
	}
}
