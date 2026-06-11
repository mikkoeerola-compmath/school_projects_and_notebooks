/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package fi.tuni.prog3.json;

import java.util.ArrayList;
import java.util.Iterator;

/**
 *
 * @author Omistaja
 */
public class ArrayNode extends Node implements Iterable<Node> {
    private ArrayList<Node> list;
    
    public ArrayNode() {
        this.list = new ArrayList<>();
    }
    
    public void add(Node node) {
        list.add(node);
    }
    
    public int size() {
        return list.size();
    }
    
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
