import java.util.Arrays;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.TimeUnit;
import java.util.function.Function;

public class Main {

    public static void main(String[] args) {
        //Organizing Inputs
        Function<Double, Double> f = (x) -> Math.sin(3 * Math.PI * Math.cos(2 * Math.PI * x) * Math.sin(Math.PI * x));
        double a = -3, b = 5;
        int n = (int) Math.pow(4, 9);
        double[] x0 = linspace(a, b, n);
        double[] q = new double[n];

        // Compute roots sequentially
        long startTime1 = System.currentTimeMillis();
        for (int i = 0; i < n; i++) {
            q[i] = fzero(f, x0[i]);
        }
        long endTime1 = System.currentTimeMillis();
        long sequentialTime = endTime1 - startTime1;

        // Compute roots in parallel
        long startTime2 = System.currentTimeMillis();
        parallelFor(0, n, i -> q[i] = fzero(f, x0[i]));
        long endTime2 = System.currentTimeMillis();
        long parallelTime = endTime2 - startTime2;

        // Print results
        System.out.println("Sequential time: " + sequentialTime + " ms");
        System.out.println("Parallel time: " + parallelTime + " ms");
    }

    public static double[] linspace(double a, double b, int n) {
        double[] result = new double[n];
        double step = (b - a) / (n - 1);
        for (int i = 0; i < n; i++) {
            result[i] = a + i * step;
        }
        return result;
    }

    public static double fzero(Function<Double, Double> f, double x0) {
        double x = x0;
        double fx = f.apply(x);
        double h = 1e-6;
        while (Math.abs(fx) > 1e-12) {
            double fp = (f.apply(x + h) - f.apply(x - h)) / (2 * h);
            double dx = -fx / fp;
            x = x + dx;
            fx = f.apply(x);
        }
        return x;
    }

    public static void parallelFor(int start, int end, Operation operation) {
        int numThreads = Runtime.getRuntime().availableProcessors();
        ExecutorService executor = Executors.newFixedThreadPool(numThreads);
        int chunkSize = (end - start) / numThreads;
        for (int i = 0; i < numThreads; i++) {
            int startIndex = start + i * chunkSize;
            int endIndex = (i == numThreads - 1) ? end : startIndex + chunkSize;
            executor.submit(() -> {
                for (int j = startIndex; j < endIndex; j++) {
                    operation.apply(j);
                }
            });
        }
        executor.shutdown();
        try {
            executor.awaitTermination(Long.MAX_VALUE, TimeUnit.NANOSECONDS);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }

    @FunctionalInterface
    public interface Operation {
        void apply(int index);
    }
}
