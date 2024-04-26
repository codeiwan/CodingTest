import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

class Solution {

    static StringTokenizer st;
    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        for (int tc = 1; tc <= 10; tc++) {
            int N = Integer.parseInt(br.readLine());
            st = new StringTokenizer(br.readLine());
            ArrayList<Integer> codes = new ArrayList<>();

            for (int i = 0; i < N; i++) {
                codes.add(Integer.parseInt(st.nextToken()));
            }

            int M = Integer.parseInt(br.readLine());
            st = new StringTokenizer(br.readLine());
            for (int i = 0; i < M; i++) {
                String command = st.nextToken();
                if (command.equals("I")) {
                    int x = Integer.parseInt(st.nextToken());
                    int y = Integer.parseInt(st.nextToken());
                    for (int j = 0; j < y; j++)
                        codes.add(x + j, Integer.parseInt(st.nextToken()));
                } else if (command.equals("D")) {
                    int x = Integer.parseInt(st.nextToken());
                    int y = Integer.parseInt(st.nextToken());
                    for (int j = 0; j < y; j++)
                        codes.remove(x);
                } else if (command.equals("A")) {
                    int y = Integer.parseInt(st.nextToken());
                    for (int j = 0; j < y; j++)
                        codes.add(Integer.parseInt(st.nextToken()));
                }
            }
            System.out.print("#" + tc + " ");
            for (int i = 0; i < 10; i++)
                System.out.print(codes.get(i) + " ");
            System.out.println();
        }
    }
}