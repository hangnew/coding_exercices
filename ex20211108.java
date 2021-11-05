// 길이가 N인 수열이 있다.
// M개의 숫자가 주어졌을 때 그 숫자가 수열에 등장했으면 1, 등장하지 않으면 0을 출력한다.

import java.util.*;
class Main {	
	public static void match(HashSet<String> set, String[] array) {
		for (int i = 0; i < array.length; i++) {
			int result = (set.contains(array[i])) ? 1 : 0;
			System.out.println(result);
		};
	}
	
	public static void main(String[] args) throws Exception {
		Scanner sc = new Scanner(System.in);
		sc.nextLine();
		HashSet<String> hashSet = new HashSet<String>(Arrays.asList(sc.nextLine().split(" ")));
		sc.nextLine();
		String[] array = sc.nextLine().split(" ");
		match(hashSet, array);
		sc.close();
	}
}
