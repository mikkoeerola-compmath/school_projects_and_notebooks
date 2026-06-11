/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package fi.tuni.prog3.sevenzipsearch;

import java.util.Scanner;
import java.io.File;
import java.io.IOException;
import org.apache.commons.compress.archivers.sevenz.SevenZArchiveEntry;
import org.apache.commons.compress.archivers.sevenz.SevenZFile;


/**
 *
 * @author Omistaja
 */
public class MainClass {
    
    public static void main(String args[]) throws IOException {
        Scanner user = new Scanner(System.in);
        System.out.println("File:");
        final String infile = user.nextLine();
        
        System.out.println("Query:");
        final String query = user.nextLine();
        System.out.println();
        
        try (SevenZFile sevenZFile = new SevenZFile(new File(infile));) {
            SevenZArchiveEntry entry = sevenZFile.getNextEntry();
            while (entry != null) {
                if (entry.getName().toLowerCase().endsWith(".txt")) {
                    System.out.println(entry.getName());
                    try {
                        Scanner reader = new Scanner(sevenZFile.getInputStream(entry));
                        String line;
                        int linenum = 1;
                        while (reader.hasNext()) {
                            line = reader.nextLine();
                            if (line.toLowerCase().contains(query.toLowerCase())) { /* katstaan onko rivilla sanaa ja tulostetaan rivi*/
                                line = line.replaceAll("(?i)"+query, query.toUpperCase());
                                System.out.println(linenum + ": " + line);
                            }
                            ++linenum;
                        }
                    } catch (IOException e) {
                        System.out.println(e);
                        break;
                    }
                }
                entry = sevenZFile.getNextEntry();
                System.out.println();
            }
            sevenZFile.close();
        } catch (IOException e) {
            System.out.println(e);
        }
    }
}
