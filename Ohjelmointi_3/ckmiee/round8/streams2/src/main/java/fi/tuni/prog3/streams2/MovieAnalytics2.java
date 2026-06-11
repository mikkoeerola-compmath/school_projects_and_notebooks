/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package fi.tuni.prog3.streams2;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.stream.Collectors;
import java.util.Map;
import java.util.Locale;

/**
 *
 * @author Omistaja
 */
public class MovieAnalytics2 {
    
    private ArrayList<Movie> MovieList;
    
    public MovieAnalytics2() {
        MovieList = new ArrayList<>();
    }
    
    public void populateWithData(String fileName) {
        try {
             var f = new BufferedReader(new FileReader(fileName));
             ArrayList<Movie> list = f.lines()
               .map(line -> line.split(";"))
               .map(m -> new Movie(m[0], Integer.parseInt(m[1]), Integer.parseInt(m[2]),
                       m[3], Double.parseDouble(m[4]), m[5]))
               .collect(ArrayList::new, ArrayList::add, ArrayList::addAll);
             
             this.MovieList = list;
             }
         
         catch(IOException e){
             System.out.println(e);
         }
    }
    
    public void printCountByDirector(int n) {
        MovieList.stream().collect(Collectors.groupingBy(m -> m.getDirector(),
                Collectors.counting()))
                .entrySet().stream()
                .sorted((Map.Entry<String, Long> ma, Map.Entry<String, Long> mb) -> {
                    int cmp = ma.getValue().compareTo(mb.getValue());
                    if (cmp == 0) {
                        return ma.getKey().compareTo(mb.getKey());
                    }
                    return -cmp;
                })
                .limit(n)
                .forEach(m ->
                  System.out.format(Locale.US,"%s: %d movies%n",
                          m.getKey(),m.getValue()));
    }
    
    public void printAverageDurationByGenre() {
        MovieList.stream().collect(Collectors.groupingBy(m -> m.getGenre(),
                Collectors.averagingInt((Movie m) -> m.getDuration())))
                .entrySet().stream()
                .sorted((Map.Entry<String, Double> ma, Map.Entry<String, Double> mb) -> {
                    int cmp = ma.getValue().compareTo(mb.getValue());
                    if (cmp == 0) {
                        return ma.getKey().compareTo(mb.getKey());
                    }
                    return cmp;
                })
                .forEach(m ->
                    System.out.format(Locale.US,
                            "%s: %.2f%n", m.getKey(), m.getValue()));
    }
    
    public void printAverageScoreByGenre() {
        MovieList.stream().collect(Collectors.groupingBy(m -> m.getGenre(),
                Collectors.averagingDouble((Movie m) -> m.getScore())))
                .entrySet().stream()
                .sorted((Map.Entry<String, Double> ma, Map.Entry<String, Double> mb) -> {
                    int cmp = ma.getValue().compareTo(mb.getValue());
                    if (cmp == 0) {
                        return ma.getKey().compareTo(mb.getKey());
                    }
                    return -cmp;
                })
                .forEach(m ->
                    System.out.format(Locale.US,
                            "%s: %.2f%n", m.getKey(), m.getValue()));
    }
}
