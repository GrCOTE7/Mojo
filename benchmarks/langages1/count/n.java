import java.io.*;

public class N {
    public static void main(String[] args) throws Exception {
        BufferedReader reader = new BufferedReader(new FileReader("apps/count/n.txt"));
        long n = Long.parseLong(reader.readLine());
        reader.close();

        long count = 0;
        for (long i = 0; i < n; i++) {
            count++;
        }

        System.out.println("Java counted to " + count);
    }
}

// Compiler avec:
//  javac apps/count/N.java
