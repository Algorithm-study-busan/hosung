package flatform;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.*;

import static java.lang.Math.min;

public class SalesSpikeDetector {
    public static void main(String[] args) {
        try {
            String csvFilePath = "sales_data.csv";
            List<int[]> salesData = readCSV(csvFilePath);
            Scanner scanner = new Scanner(System.in);
            int threshold = scanner.nextInt();
            int timePeriod = scanner.nextInt();

            Map<Integer, Integer> results = detectSalesSpike(salesData, threshold, timePeriod);
            if (results.isEmpty()) {
                System.out.println("No sales spike detected");

            } else {
                for (Map.Entry<Integer, Integer> entry : results.entrySet()) {
                    System.out.println("Item ID: " + entry.getKey() + ", Time Period: " + entry.getValue() + " minutes");
                }
            }
        } catch (IOException e) {
            System.out.println("Error reading CSV file: " + e.getMessage());
        }
    }

    public static List<int[]> readCSV(String csvFilePath) throws IOException {
        List<int[]> data = new ArrayList<>();
        try (BufferedReader reader = new BufferedReader(new FileReader(csvFilePath))) {
            reader.readLine(); // Skip header
            String line;

            while ((line = reader.readLine()) != null) {
                String[] parts = line.split(",");
                int[] row = new int[parts.length - 1];
                for (int i = 0; i < row.length; i++) {
                    row[i] = Integer.parseInt(parts[i + 1]);
                }
                data.add(row);
            }
        }
        return data;
    }

    public static Map<Integer, Integer> detectSalesSpike(List<int[]> salesData, int threshold, int period) {
        List<int[]> total = new ArrayList<>();
        Map<Integer, Integer> results = new HashMap<>();
        int[] sum = new int[10];
        int[] ans = new int[10];

        for (int i = 0; i < 10; i++) {
            ans[i] = 987654321;
        }
        total.add(sum);
        for (int[] row : salesData) {
            for (int i = 0; i < row.length; i++) {
                sum[i] += row[i];
            }
            int[] copy = new int[10];
            System.arraycopy(sum, 0, copy, 0, 10);
            total.add(copy);
        }

        for (int i = 0; i < total.size(); i++) {
            for (int j = 0; j < i; j++) {
                for (int k = 0; k < 10; k++) {
                    if (total.get(i)[k] - total.get(j)[k] >= threshold && i - j <= period) {
                        ans[k] = min(ans[k], i - j);
                    }
                }
            }
        }

        for (int i = 0; i < 10; i++) {
            if (ans[i] == 987654321) continue;
            results.put(i + 1, ans[i]);
        }
        return results;
    }

}
