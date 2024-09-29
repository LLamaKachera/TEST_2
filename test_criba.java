public class Criba1{
    public static void Criba(int n) {
        boolean[] primo = new boolean[n + 2];
        primo[0] = primo[1] = false;
        int i = 2;
        while (i * i <= n) {
            if (primo[i]) {
                for (int j = i * i; j <= n; j += i) {
                    primo[j] = false;
                }
            }
            i = i + 1;
        }
    }

    public static void main(String[] args) {
        int n = 5000;
        boolean[] primo = new boolean[n + 2];
        for (int i = 0; i < primo.length; i++) {
            primo[i] = true;
        }
        Criba(n);
        
        long a, b, d;        
        a = System.nanoTime();
        Criba(n);
        b = System.nanoTime();
        d = b - a;
        System.out.println(d);
    }
}
    