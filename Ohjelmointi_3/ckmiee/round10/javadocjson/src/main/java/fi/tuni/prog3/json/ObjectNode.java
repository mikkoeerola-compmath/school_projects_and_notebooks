/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package fi.tuni.prog3.json;

import java.util.TreeMap;
import java.util.Iterator;

/**
 * A class for representing a JSON object.
 */
public class ObjectNode extends Node implements Iterable<String> {
    private TreeMap<String, Node> map;
    
    /**
         * Constructs an initially empty JSON object node.
         */
    public ObjectNode() {
        
        this.map = new TreeMap<>();
    }
    
    /**
         * Returns the number of JSON nodes stored under this JSON object.
         * @return the number of JSON nodes under this JSON object.
         */
    public int size() {
        
        return map.size();
    }
    
    /**
         * Returns the JSON node stored under the given name.
         * @param name - the name of the name-node pair whose node should be returned.
         * @return the JSON node corresponding to name, or null if such node does not exist.
         */
    public Node get(String name) {
        
        return map.get(name);
    }
    
    /**
         * <p> Stores a name - JSON node pair into this JSON object.
         * If a name-node pair with the same name already exists,
         * the previously existing node will be replaced.</p>
         * @param name - the name of the name-node pair.
         * @param node - the JSON node of the name-node pair.
         */
    public void set(String name, Node node) {
        
        map.put(name, node);
    }
    
    /**
         * <p>Returns a String iterator that iterates the names of the
         * name-node pairs stored in this JSON object in natural String order.
         * </p>
         * @return a String iterator that iterates the names of the stored name-node pairs in natural String order.
         */
    @Override
    public Iterator<String> iterator(){
        
        return map.keySet().iterator();
    }
}
