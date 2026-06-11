/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package fi.tuni.prog3.json;

import java.util.ArrayList;
import java.util.Iterator;

/**
 *A class for representing a JSON array.
 */
public class ArrayNode extends Node implements Iterable<Node> {
    private ArrayList<Node> list;
    
    /** 
    * Constructs an initially empty JSON array node.
    */
    public ArrayNode() {
        this.list = new ArrayList<>();
    }
    
    /**
         * Returns the number of JSON nodes stored in this JSON array.
         * @return the number of JSON nodes in this JSON array.
         */
    public int size() {
        
        return list.size();
    }
    
    /**
         * Adds a new JSON node to the end of this JSON array.
         * @param node - the new JSON node to be added.
         */
    public void add(Node node) {
        
        list.add(node);
    }
    
    /**
         * <p> Returns a Node iterator that iterates the JSON nodes 
         * stored in this JSON array.</p>
         * @return a Node iterator that iterates the JSON nodes stored in this JSON array.
         */
    @Override
    public Iterator<Node> iterator() {
        
        return list.iterator();
    }
    /*private class ArrayNodeIterator implements Iterator<Node> {
        private Node next;
        
        @Override
        public boolean hasNext() {
            
        }
        
        @Override
        public Node next
    }*/
    
}
