/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 */

/**
 *
 * @author ckmiee
 */

import java.util.Scanner;

public class EkaJavaProjekti {

    public static void main(String[] args) {
        Scanner myScanner = new Scanner(System.in);
        System.out.println("Enter numbers:");
        String rivi = myScanner.nextLine();
        String[] numbers = rivi.split(" ");
        
        Double sum = 0.0;
        for (String s : numbers) {
            Double x = Double.parseDouble(s);
            sum += x;
        }
        Double mean = sum/numbers.length;
        System.out.println("Mean: " + mean);
    }
}
