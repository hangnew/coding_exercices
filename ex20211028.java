// 리그에 속해있는 팀의 수 n이 주어지고 각 팀은 자신을 제외한 모든 팀과 한 경기씩 치루어 순위를 가리는 스포츠 리그전에서 치루어지는 경기의 수를 구하는 프로그램을 작성하십시오.
// 2팀이면 1경기, 3팀이면 3경기, 4팀이면 6경기가 치루어 집니다.

import java.io.*;
import java.util.*;

class Main {
	public static void main(String[] args) throws Exception {
		Scanner sc = new Scanner(System.in);
		int team = sc.nextInt();
		int match = 0;
		for (int i = 1; i < team; i++) {
			match += i;
		}
		System.out.println(match);
		sc.close();
	}
}
