/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package fi.tuni.prog3.json;

import java.util.TreeMap;
import java.util.Iterator;

/**
 *
 * @author Omistaja
 */
public class ObjectNode extends Node implements Iterable<String> {
    private TreeMap<String, Node> map;
    
    public ObjectNode() {
        this.map = new TreeMap<>();
    }
    
    public Node get(String key) {
        return map.get(key);
    }
    
    public void set(String key, Node node) {
        map.put(key, node);
    }
    
    public int size() {
        return map.size();
    }
    
    @Override
    public Iterator<String> iterator(){
        return map.keySet().iterator();
    }
}
