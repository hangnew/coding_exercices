// 혜지는 자신의 컴퓨터로 코딩을 하던 중, 자신의 코드가 통째로 지워지는 현상을 겪었다. 
// 여러 번의 시행착오 끝에, 키보드를 마지막으로 누른 후 c초 동안 자신의 코드가 그대로 남아있다가 (c+1)초가 경과하는 순간 모든 코드가 지워지는 것을 알게 되었다. 
// 혜지는 오기가 생겨 과연 자신의 코드가 지워지는게 먼저인지 아니면 자신이 코드를 완성하는 게 먼저인지 자신의 고장난 컴퓨터와 대결해보고 싶었다. 
// 혜지가 키보드를 총 N번 누른다고 할 때, 코딩을 시작한 이후 몇 초가 경과하고 키보드를 쳤는지에 대한 N개의 정보를 이용하여 코딩을 마쳣을 때 총 몇 글자가 남아있는지 계산하여라.

import java.util.*;

class Main {
	
	public static void countdown(int sec, int[] array) {
		// array.length == 1일 때 글자수 1개
		int count = 1;
		for (int i = 0; i < array.length - 1; i++) {
			count = ((array[i + 1] - array[i]) <= sec) ? count + 1 : 1;
		}
		System.out.println(count);
	}
	
	public static void main(String[] args) throws Exception {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int c = sc.nextInt();
		int[] tArray = new int[n];
		for (int i = 0; i < tArray.length; i++) {
			tArray[i] = sc.nextInt();
		}
		countdown(c, tArray);
		sc.close();
	}
}
