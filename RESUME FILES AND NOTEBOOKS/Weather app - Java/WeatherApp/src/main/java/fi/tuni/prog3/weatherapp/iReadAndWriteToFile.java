package fi.tuni.prog3.weatherapp;

import java.util.List;
import java.util.Set;
/**
 * Interface with methods to read from a file and write to a file.
 */
public interface iReadAndWriteToFile {

    /**
     * Adds to SearchHisotry list in JSON file.
     * 
     * @param fileName name of the file to write to.
     * @param lastSearch of the file to write to.
     * @return true if the write was successful, otherwise false.
     * @throws Exception if the method e.g., cannot write to a file.
     */
    public boolean addSearchHistory(String fileName, String lastSearch) throws Exception;

    /**
     * Adds to Favorite list in JSON file.
     * 
     * @param favorite of the file to write to.
     * @param fileName name of the file to write to.
     * @return true if the write was successful, otherwise false.
     * @throws Exception if the method e.g., cannot write to a file.
     */
    public boolean addFavorite(String fileName, String favorite) throws Exception;

    /**
     * Removes the favorite from saved JSON file.
     * 
     * @param favorite of the file to write to.
     * @param fileName name of the file to write to.
     * @return true if the write was successful, otherwise false.
     * @throws Exception if the method e.g., cannot write to a file.
     */
    public boolean removeFavorite(String fileName, String favorite) throws Exception;

    /**
     * Removes the search history from saved JSON file.
     * 
     * @param lastSearch of the file to write to.
     * @return true if the write was successful, otherwise false.
     * @throws Exception if the method e.g., cannot write to a file.
     */
    public boolean clearSearchHistory(String fileName) throws Exception;

    /**
     * Removes the favorites from saved JSON file.
     * 
     * @param fileName name of the file to write to.
     * @return true if the clear was successful, otherwise false.
     * @throws Exception if the method e.g., cannot write to a file.
     */
    public boolean clearFavorites(String fileName) throws Exception;

    /**
     * Returns the favorites from the saved JSON file as a list.
     * 
     * @param fileName name of the file to write to.
     * @return set of favorites.
     * @throws Exception if the method cannot read from a file.
     */
    public Set<String> getFavorites(String fileName) throws Exception;

    /**
     * Returns the SearchHistory from the saved JSON file as a list.
     * 
     * @param fileName name of the file to write to.
     * @return list of SearchHistory.
     * @throws Exception if the method cannot read from a file.
     */
    public List<String> getSearchHistory(String fileName) throws Exception;

    /**
     * Removes specific search history from saved JSON file.
     * 
     * @param lastSearch of the file to write to.
     * @param fileName name of the file to write to.
     * @return true if the removal was successful, otherwise false.
     * @throws Exception if the method e.g., cannot write to a file.
     */
    public boolean removeSearchHistory(String fileName, String lastSearch) throws Exception;

}
