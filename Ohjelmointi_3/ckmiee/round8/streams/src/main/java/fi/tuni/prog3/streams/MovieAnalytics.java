/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package fi.tuni.prog3.streams;

import java.util.function.Consumer;
import java.util.ArrayList;
import java.io.FileReader;
import java.io.BufferedReader;
import java.io.IOException;
import java.util.stream.Stream;
import java.util.Comparator;
/**
 *
 * @author Omistaja
 */
public class MovieAnalytics {
    private ArrayList<Movie> MovieList;
    
    public MovieAnalytics() {
        MovieList = new ArrayList<>();
    }
    
    public static Consumer<Movie> showInfo() {
        
        return p -> System.out.format("%s (By %s, %d)%n", p.getTitle(),
                        p.getDirector(), p.getReleaseYear());
        
        /*return new Consumer<Movie>()  {
            @Override
            public void accept(Movie m) {
                System.out.format("%s (by %s, %d)", m.getTitle(),
                        m.getDirector(), m.getReleaseYear());
            }
        }*/
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
    
    Comparator<Movie> compMovie = new Comparator<>() {
        @Override
        public int compare(Movie t, Movie p) {
            return t.getReleaseYear() > p.getReleaseYear()? 1 :(
                    t.getReleaseYear() < p.getReleaseYear()? -1 :
                    t.getTitle().compareTo(p.getTitle()));
        }
    };
    
    /*Comparator<Movie> compMovie = (Movie t, Movie p) -> 
            (t.getReleaseYear() <= p.getReleaseYear())? 1 : 
                    t.getReleaseYear() > p.getReleaseYear()? -1 :
                    (t.getTitle().compareTo(p.getTitle()));
    */
    public Stream<Movie> moviesAfter(int year) {
        return this.MovieList.stream().filter(p -> (p.getReleaseYear() >= year))
                .sorted(compMovie);
    }
    
    public Stream<Movie> moviesBefore(int year) {
        return this.MovieList.stream().filter(p -> (p.getReleaseYear() <= year))
                .sorted(compMovie);
    }
    
    public Stream<Movie> moviesBetween(int yearA, int yearB) {
        return this.MovieList.stream().filter(p -> (p.getReleaseYear() >= yearA
                && p.getReleaseYear() <= yearB))
                .sorted(compMovie);
    }
    
    public Stream<Movie> moviesByDirector(String director) {
        return this.MovieList.stream().filter(p -> 
                (p.getDirector().compareTo(director) == 0))
                .sorted(compMovie);
    }
}
