import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {
    static boolean isSosu(int num) {
        if (num == 1) {
            return false;
        }

        for (int j = 2; j < num; j++) {
            if (num % j == 0) {
                return false;
            }
        }

        return true;
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int x = Integer.parseInt(br.readLine());
        String[] numbers = br.readLine().split(" ");

        int count = 0;
        for (int i = 0; i < numbers.length; i++) {
            int arg = Integer.parseInt(numbers[i]);

            if (isSosu(arg)) {
                count++;
            }
        }

        System.out.println(count);
    }
}