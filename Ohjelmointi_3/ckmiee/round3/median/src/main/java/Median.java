import java.util.Scanner;
import java.util.Arrays;

/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 */

/**
 *
 * @author ckmiee
 */
public class Median {

    public static void main(String[] args) {
        Scanner myScanner = new Scanner(System.in);
        System.out.println("Enter numbers:");
        String rivi = myScanner.nextLine();
        String[] numbers = rivi.split(" ");
        
        Arrays.sort(numbers, (s1, s2) -> {
            double a = Double.parseDouble(s1);
            double b = Double.parseDouble(s2);
            return a < b ? -1 : (b<a ? 1 : 0);
                });
        
        double median;
        if(numbers.length % 2 != 0) {
            median = Double.parseDouble(numbers[numbers.length/2]);
        } else {
            double a = Double.parseDouble(numbers[(numbers.length-1)/2]);
            double b = Double.parseDouble(numbers[numbers.length/2]);
            median = (a+b)/2;
        }
        
        System.out.println("Median: " + median);
    }
}
