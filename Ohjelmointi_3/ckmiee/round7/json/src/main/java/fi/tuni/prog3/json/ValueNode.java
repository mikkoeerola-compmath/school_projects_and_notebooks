/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package fi.tuni.prog3.json;

/**
 *
 * @author Omistaja
 */
public class ValueNode<T> extends Node{
    private T value;
    
    public ValueNode() {
        this.value = null;
    }
    
    public ValueNode(T d) {
        this.value = d;
    }
    /*
    ValueNode(boolean b) {
        this.value = b;
    }
    
    ValueNode(String s) {
        this.value = s;
    }*/
    
    public <T> boolean isNumber() {
        try {
            if (value == null) {return false;}
            Double.parseDouble(value.toString());
            return true;
        } catch (NumberFormatException e) {
            return false;
        }
    }
    
    public boolean isBoolean() {
        return value instanceof Boolean;
    }
    
    public boolean isString() {
        return value instanceof String;
    }
    
    public boolean isNull() {
        return value == null;
    }
    
    public <T> double getNumber() {
        return ((Number) value).doubleValue();
    }
    
    public <T> boolean getBoolean() {
        return (boolean) value;
    }
    
    public <T> String getString() {
        return (String) value;
    }
    
    public Object getNull() {
        return value;
    } 
}
