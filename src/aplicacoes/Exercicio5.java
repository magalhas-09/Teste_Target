package aplicacoes;

import java.util.Scanner;

public class Exercicio5 {

	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);

		System.out.print("Digite a string que deseja inverter: ");
		String original = sc.nextLine();

		String invertida = Exercicio5(original);

		System.out.println("String invertida: " + invertida);

		sc.close();

	}

	private static String Exercicio5(String str) {

		char[] caracteres = str.toCharArray();
		int n = caracteres.length;

		for (int i = 0; i < n / 2; i++) {

			char temp = caracteres[i];
			caracteres[i] = caracteres[n - i - 1];
			caracteres[n - i - 1] = temp;

		}

		return new String(caracteres);

	}
}
