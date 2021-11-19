// 문자열을 입력하고 입력된 문자열의 문자를 앞뒤로 번갈아 출력하는 프로그램을 작성하십시오.

// 입력 : 임의의 문자열 (100자 이내)
// 출력 : 입력된 문자열의 앞과 뒤가 번갈아 출력된 형태

import java.util.*;

class Main {
  
	public static void main(String[] args) throws Exception {
		Scanner sc = new Scanner(System.in);
		String words = sc.nextLine();
    sc.close();
		for (int i = 0; i < words.length(); i++) {
			int j = words.length() - i - 1;
			if (i > j) {
				break;
			} else if (i == j) {
				System.out.print(words.charAt(i));
			} else {
				System.out.print("" + words.charAt(i) + words.charAt(j));
			}
		}
	}
  
}
