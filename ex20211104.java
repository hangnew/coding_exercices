// 입력된 수가 소수(Prime Number)인지를 판별하는 프로그램을 작성하십시오.
// O(\sqrt{n})의 시간에 동작하는 알고리즘으로 문제를 해결하는 것을 권장합니다.

import java.util.*;

class Main {
	public static void main(String[] args) throws Exception {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		System.out.println(isPrime(n));
		sc.close();
	}
	
	public static String isPrime(int number) {
		if (number == 1) {
			return "False";
		} else if (number == 2) {
			return "True";
		} else if (number % 2 == 0) {
			return "False";
		}
		for (int i = 3; i < Math.sqrt(number); i += 2){
			if (number % i == 0) {
				return "False";
			}
		}
		return "True";
	}
}
