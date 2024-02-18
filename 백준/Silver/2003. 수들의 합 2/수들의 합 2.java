import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        st = new StringTokenizer(br.readLine());
        int[] S = new int[N + 1];
        for (int i = 1; i <= N; i++) {
            S[i] = S[i - 1] + Integer.parseInt(st.nextToken());
        }
        int count = 0, sum, s = 0, e = 1;
        while(e <= N) {
            sum = S[e] - S[s];
            if (sum == M) {
                count++;
                s++;
            } else if (sum > M) {
                s++;
            } else if (sum < M) {
                e++;
            }
        }
        System.out.println(count);
    }
}
