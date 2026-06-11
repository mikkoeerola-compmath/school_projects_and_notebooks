package fi.tuni.prog3.weatherapp;

import java.util.List;
import org.junit.jupiter.api.Test;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.Set;
import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.AfterAll;


import static org.junit.jupiter.api.Assertions.assertTrue;
import static org.junit.jupiter.api.Assertions.assertFalse;


import org.junit.jupiter.api.MethodOrderer;
import org.junit.jupiter.api.Order;
import org.junit.jupiter.api.TestMethodOrder;


// Test class for ReadAndWriteToFile
@TestMethodOrder(MethodOrderer.OrderAnnotation.class) 
public class ReadAndWriteToFileTest {


    // Object to test
    ReadAndWriteToFile fileHandling = new ReadAndWriteToFile();
    
    // Test file name
    static String testFileName = "SavedDataTest.json";

    // Creates a test file which will be deleted after the tests
    @BeforeAll
    public static void createFile() throws IOException {
        Files.createFile(Paths.get(testFileName));
        String initialContent = "{\"favorites\":[],\"searchHistory\":[]}";
        Files.write(Paths.get(testFileName), initialContent.getBytes());
    }

    @AfterAll
    public static void deleteFile() throws IOException {
        Files.deleteIfExists(Paths.get(testFileName));
    }



    @Test
    @Order(1)
    public void testAddFavorite() throws IOException {
        String favorite = "Tampere";
        fileHandling.addFavorite(testFileName, favorite);
        String favorite2 = "Kotka";
        fileHandling.addFavorite(testFileName, favorite2);

        // Checks if the file contains the favorite
        String fileContent = new String(Files.readAllBytes(Paths.get(testFileName)));
        System.out.println("File content: " + fileContent + " After adding " + favorite + " and " + favorite2);
        assertTrue(fileContent.contains(favorite));
    }

    @Test
    @Order(2)
    public void testaddSearchHistory() throws IOException {
        String lastSearch = "Lahti";
        fileHandling.addSearchHistory(testFileName, lastSearch);
        String lastSearch2 = "Helsinki";
        fileHandling.addSearchHistory(testFileName, lastSearch2);

        // Checks if the file contains the last search
        String fileContent = new String(Files.readAllBytes(Paths.get(testFileName)));
        System.out.println("File content: " + fileContent + " After adding " + lastSearch + " and " + lastSearch2);
        assertTrue(fileContent.contains(lastSearch));
    }

    @Test
    @Order(3)
    public void testremoveFavorite() throws IOException {

        String favorite = "Tampere";
        // Removes the favorite
        fileHandling.removeFavorite(testFileName, favorite);

        // Checks if the file contains the favorite
        String fileContent = new String(Files.readAllBytes(Paths.get(testFileName)));
        System.out.println("File content: " + fileContent + " After removing " + favorite);
        assertFalse(fileContent.contains(favorite));
    }

    @Test
    @Order(4)
    public void testremoveSearchHistory() throws IOException {

        String lastSearch = "Lahti";
        fileHandling.removeSearchHistory(testFileName, lastSearch);

        // Checks if the file contains the favorite
        String fileContent = new String(Files.readAllBytes(Paths.get(testFileName)));
        System.out.println("File content: " + fileContent + " After removing " + lastSearch);
        assertFalse(fileContent.contains(lastSearch));
    }


    @Test
    @Order(5)
    public void testgetSearchHistory() throws IOException {
        List<String> searchHistory = fileHandling.getSearchHistory(testFileName);

        // Prinst the search history
        System.out.println("Search history: " + searchHistory);

    }

    @Test
    @Order(6)
    public void testgetFavorites() throws IOException {
        Set<String> favorites = fileHandling.getFavorites(testFileName);

        // Prints the search history
        System.out.println("Favourites: " + favorites);
    }

    @Test
    @Order(7)
    public void testClearSearchHistory() throws IOException {
        fileHandling.clearSearchHistory(testFileName);

        // Checks if the search history is empty
        List<String> searchHistory = fileHandling.getSearchHistory(testFileName);
        assertTrue(searchHistory.isEmpty());
    }

    @Test
    @Order(8)
    void testclearFavorites() throws IOException {

        fileHandling.clearFavorites(testFileName);
        // Checks if the search history is empty
        Set<String> favorites = fileHandling.getFavorites(testFileName);
        assertTrue(favorites.isEmpty());
    }

}