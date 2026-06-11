/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 */

package fi.tuni.prog3.shapes;

import java.text.DecimalFormat;
import java.text.DecimalFormatSymbols;
import java.util.Locale;

/**
 *
 * @author Omistaja
 */
public class Circle implements IShapeMetrics {

    private double radius;
    
    public Circle(double r) {
        this.radius = r;
    }
    
    @Override
    public String toString() {
        DecimalFormatSymbols symbolit = new DecimalFormatSymbols(new Locale("fi", "FI"));
        symbolit.setDecimalSeparator('.');
        DecimalFormat df = new DecimalFormat("#.00", symbolit);
        String tuloste_r = df.format(this.radius);
        
        return String.format("Circle with radius: " + tuloste_r);
    }
    
    @Override
    public double area() {
        return PI*this.radius*this.radius;
    }
    
    @Override
    public double circumference() {
        return PI*this.radius*2;
    }
    
    @Override
    public String name() {
        return "circle";
    }
}
