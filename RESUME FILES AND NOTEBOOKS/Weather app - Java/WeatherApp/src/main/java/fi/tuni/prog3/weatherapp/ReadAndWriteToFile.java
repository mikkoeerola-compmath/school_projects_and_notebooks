package fi.tuni.prog3.weatherapp;

import com.fasterxml.jackson.databind.ObjectMapper;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.nio.file.Path;
import java.util.List;
import java.util.Set;
import com.fasterxml.jackson.databind.JsonNode;


/**
 * Class to read and write to a saved file
 * @author Valtteri Sutelainen
 */
public class ReadAndWriteToFile implements iReadAndWriteToFile {

    // SavedData object to store data from JSON file
    private SavedData savedData = new SavedData();

    // Capitalizes the first letter of the string
    private String capitalizeFirstLetter(String str) {
        if (str == null || str.isEmpty()) {
            return str;
        } else {
            return str.substring(0, 1).toUpperCase() + str.substring(1).toLowerCase();
        }
    }

    // Reads the saved data from the file SavedData.json
    // userdata.json includes {"favorites":[],"searchHistory":[]} where list of
    // favorites and search history are stored
    // If the file does not exist or has not right format it will create a new one
    private SavedData readSavedDataFromFile(String fileName) throws IOException {
        ObjectMapper mapper = new ObjectMapper();
        Path filePath = Paths.get(fileName);
    
        // Check if file exists, if not create a new one with default SavedData
        if (!Files.exists(filePath)) {
            SavedData defaultData = new SavedData();
            String defaultDataJson = mapper.writeValueAsString(defaultData);
            Files.write(filePath, defaultDataJson.getBytes());
        }
    
        // Read data from file
        String existingData = new String(Files.readAllBytes(filePath));
        JsonNode rootNode = mapper.readTree(existingData);
    
        // Check if the JSON has the 'favorites' and 'searchHistory' keys if not create a new one with default SavedData
        if (!rootNode.has("favorites") || !rootNode.has("searchHistory")) {
            SavedData defaultData = new SavedData();
            String defaultDataJson = mapper.writeValueAsString(defaultData);
            Files.write(filePath, defaultDataJson.getBytes());
        }
    
        return mapper.readValue(existingData, SavedData.class);
    }

    @Override
    public boolean addSearchHistory(String fileName, String lastSearch) throws IOException {
        try {
            ObjectMapper mapper = new ObjectMapper();

            // Read existing data from file
            SavedData existingData = readSavedDataFromFile(fileName);

            // Get searchHistory list and add new search
            // Add new search to searchHistory list
            existingData.getSearchHistory().add(capitalizeFirstLetter(lastSearch));

            // Write data back to file
            String updatedDataJson = mapper.writeValueAsString(existingData);
            Files.write(Paths.get(fileName), updatedDataJson.getBytes());

            return true;
        } catch (IOException e) {
            return false;
        }
    }

    // Adds to Favorite list in saved JSON file
    @Override
    public boolean addFavorite(String fileName, String favorite) throws IOException {
        try {
            ObjectMapper mapper = new ObjectMapper();
            SavedData existingData = readSavedDataFromFile(fileName);

            // Get searchHistory list and add new search
            // Add new search to searchHistory list
            existingData.getFavorites().add(capitalizeFirstLetter(favorite));

            // Write data back to file
            String updatedDataJson = mapper.writeValueAsString(existingData);
            Files.write(Paths.get(fileName), updatedDataJson.getBytes());

            return true;
        } catch (IOException e) {
            return false;
        }
    }

    // Removes the favorite from saved JSON file
    @Override
    public boolean removeFavorite(String fileName, String favorite) throws IOException {

        ObjectMapper mapper = new ObjectMapper();
        SavedData existingData = readSavedDataFromFile(fileName);
        // Remove favorite from the list
        Set<String> favorites = existingData.getFavorites();
        if (favorites.contains(favorite)) {
            favorites.remove(favorite);
            existingData.setFavorites(favorites);

            // Write data back to file
            String updatedDataJson = mapper.writeValueAsString(existingData);
            Files.write(Paths.get(fileName), updatedDataJson.getBytes());

            return true;
        }
        return false;
    }

    @Override
    public boolean removeSearchHistory(String fileName, String lastSearch) throws IOException {
        ObjectMapper mapper = new ObjectMapper();
        SavedData existingData = readSavedDataFromFile(fileName);

        // Remove search from the list
        List<String> searchHistory = existingData.getSearchHistory();
        if (searchHistory.contains(lastSearch)) {
            searchHistory.remove(lastSearch);
            existingData.setSearchHistory(searchHistory);

            // Write data back to file
            String updatedDataJson = mapper.writeValueAsString(existingData);
            Files.write(Paths.get(fileName), updatedDataJson.getBytes());

            return true;
        }

        return false;
    }

    // Removes the search history from saved JSON file
    @Override
    public boolean clearSearchHistory(String fileName) throws IOException {

        try {
            ObjectMapper mapper = new ObjectMapper();
            SavedData existingData = readSavedDataFromFile(fileName);
            // Clear search history
            List<String> searchHistory = existingData.getSearchHistory();
            searchHistory.clear();
            existingData.setSearchHistory(searchHistory);

            // Write data back to file
            String updatedDataJson = mapper.writeValueAsString(existingData);
            Files.write(Paths.get(fileName), updatedDataJson.getBytes());

            return true;
        } catch (IOException e) {
            return false;
        }
    }

    // Removes the favorites from saved JSON file
    @Override
    public boolean clearFavorites(String fileName) throws IOException {

        try {
            ObjectMapper mapper = new ObjectMapper();
            SavedData existingData = readSavedDataFromFile(fileName);

            // Clear favorites
            Set<String> favorites = existingData.getFavorites();
            favorites.clear();
            existingData.setFavorites(favorites);

            // Write data back to file
            String updatedDataJson = mapper.writeValueAsString(existingData);
            Files.write(Paths.get(fileName), updatedDataJson.getBytes());

            return true;
        } catch (IOException e) {
            return false;
        }
    }

    @Override
    public Set<String> getFavorites(String fileName) throws IOException {
        SavedData existingData = readSavedDataFromFile(fileName);
        return existingData.getFavorites();
    }

    @Override
    public List<String> getSearchHistory(String fileName) throws IOException {
        SavedData existingData = readSavedDataFromFile(fileName);
        return existingData.getSearchHistory();
    }

}
