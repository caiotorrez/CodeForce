import java.util.Scanner;

public class Main {

	public static void main(String[] args) {

		Scanner in = new Scanner(System.in);

		int numberOfBooks = in.nextInt();
		long freeMinutes = in.nextLong();
		int[] bookMinutes = new int[numberOfBooks];
		for (int i = 0; i < numberOfBooks; i++) {
			bookMinutes[i] = in.nextInt();
		}
		
		int right = 0;
		int left = 0;
		long soma = 0;
		long total = 0;
		while (left < numberOfBooks) {

			soma += bookMinutes[left++];
			while (soma > freeMinutes) {
				soma -= bookMinutes[right++];
			}
			if (total < left - right) {
				total = left - right;
			}
		}
		System.out.println(total);
		in.close();
	}
}
