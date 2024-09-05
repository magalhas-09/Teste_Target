package aplicacoes;

public class Exercicio2 {

	public static void main(String[] args) {
		
		int numero = 52; // Pode ser substituído por qualquer outro valor
        if (isFibonacci(numero)) {
            System.out.println("O número " + numero + " pertence à sequência de Fibonacci.");
        } else {
            System.out.println("O número " + numero + " NÃO pertence à sequência de Fibonacci.");
        }
    }

    public static boolean isFibonacci(int n) {
        if (n == 0 || n == 1) {
            return true;
        }

        int prev = 0;
        int curr = 1;

        while (curr < n) {
            int next = prev + curr;
            prev = curr;
            curr = next;
        }

        return curr == n;

	}

}
