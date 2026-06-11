/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package fi.tuni.prog3.json;

/**
 *A class for representing a JSON value. The value can be either a double, a boolean, a String or null.
 */
public class ValueNode extends Node{
    private String vals;
    private double vald;
    private boolean valb;
    private Object valo;
    
    /**
         * Constructs a JSON value node that stores the null value.
         */
    public ValueNode() {
        
        this.valo = null;
    }
    
    /**
         * Constructs a JSON value node that stores the given double value.
         * @param value - The double value to store in the new JSON value node.
         */
    public ValueNode(double value) {
        
        this.vald = value;
    }
    
    /**
         * Constructs a JSON value node that stores the given boolean value.
         * @param value - The boolean value to store in the new JSON value node.
         */
    public ValueNode(boolean value) {
        
        this.valb = value;
    }
    
    /**
         * Constructs a JSON value node that stores the given string.
         * @param value - The string to store in the new JSON value node.
         * @throws IllegalStateException - if the parameter value is null.
         */
    public ValueNode(String value) {
        
        this.vals = value;
    }
    
    /**
         * Checks whether this value node stores a number (double).
         * @return true if this node stores a double value, otherwise false.
         */
    public boolean isNumber() {
        
        try {
            if (vals == null) {return false;}
            Double.parseDouble(vals.toString());
            return true;
        } catch (NumberFormatException e) {
            return false;
        }
    }
    
    /**
         * Checks whether this value node stores a boolean value.
         * @return true if this node stores a boolean value, otherwise false.
         */
    public boolean isBoolean() {
        
        return valo instanceof Boolean;
    }
    
    /**
         * Checks whether this value node stores a string.
         * @return true if this node stores a string, otherwise false.
         */
    public boolean isString() {
        
        return vals instanceof String;
    }
    
    /**
         * Checks whether this value node stores null.
         * @return true if this node stores null, otherwise false.
         */
    public boolean isNull() {
        
        return vals == null;
    }
    
    /**
         * Returns the stored value as a number (double).
         * @return the stored number as a double value.
         * @throws IllegalStateException - if the stored value is not a number.
         */
    public double getNumber() {
        
        return ((Number) vald).doubleValue();
    }
    
    /**
         * Returns the stored value as a boolean value.
         * @return the stored boolean value.
         * @throws IllegalStateException - if the stored value is not a boolean value. 
         */
    public boolean getBoolean() {
        
        return (boolean) valb;
    }
    
    /**
         * Returns the stored value as a string.
         * @return the stored string.
         * @throws IllegalStateException - if the stored value is not a string.
         */
    public String getString() {
        
        return (String) vals;
    }
    
    /**
         * Returns the stored value as null.
         * @return null.
         * @throws IllegalStateException - if the stored value is not null.
         */
    public Object getNull() {
        
        return vals;
    } 
}
