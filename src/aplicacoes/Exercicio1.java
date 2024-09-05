package aplicacoes;

public class Exercicio1 {

	public static void main(String[] args) {
		
		int indice = 13;
		int soma = 0;
		int K = 0;

		while (K < indice) {
		    K = K + 1;
		    soma = soma + K;
		}

		System.out.println("O Valor final da soma é: "+ soma);
}

}