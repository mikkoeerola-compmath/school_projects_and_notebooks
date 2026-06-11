/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package fi.tuni.prog3.shapes;

import java.text.DecimalFormat;
import java.text.DecimalFormatSymbols;
import java.util.Locale;

/**
 *
 * @author Omistaja
 */
public class Rectangle implements IShapeMetrics {
    private double height;
    private double width;
    
    public Rectangle(double h, double w) {
        this.height = h;
        this.width = w;
    }
    
    @Override
    public String toString() {
        DecimalFormatSymbols symbolit = new DecimalFormatSymbols(new Locale("fi", "FI"));
        symbolit.setDecimalSeparator('.');
        DecimalFormat df = new DecimalFormat("#.00", symbolit);
        String tuloste_h = df.format(this.height);
        String tuloste_w = df.format(this.width);
        
        return String.format("Rectangle with height " + tuloste_h + " and width "
                + tuloste_w);
    }
    
    @Override
    public String name() {
        return "rectangle";
    }
    
    @Override
    public double area() {
        return this.height*this.width;
    }
    
    @Override
    public double circumference() {
        return 2*this.height+2*this.width;
    }
    
}
