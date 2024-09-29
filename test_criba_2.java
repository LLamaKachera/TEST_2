public class Criba {
    
    public static void criba(int n, boolean[] primo) {
        primo[0] = primo[1] = false;
        int i = 2;
        
        while (i * i <= n) {
            if (primo[i]) {
                for (int j = i * i; j <= n; j += i) {
                    primo[j] = false;
                }
            }
            i++;
        }
    }

    public static void main(String[] args) {
        int n = 25;
        boolean[] primo = new boolean[n + 2];
        
        // Inicializa todos los elementos como verdaderos
        for (int i = 0; i < primo.length; i++) {
            primo[i] = true;
        }

        criba(n, primo);

        // Imprime los números primos
        for (int i = 2; i < n; i++) {
            if (primo[i]) {
                System.out.println(i);
            }
        }
    }
}
