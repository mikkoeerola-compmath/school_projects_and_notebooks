package fi.tuni.prog3.weatherapp;

import java.util.ArrayList;
import java.util.List;
import java.util.Set;
import java.util.HashSet;

/**
 * Class to handle saved data
 * 
 * @author Valtteri Sutelainen
 */
public class SavedData {
    private Set<String> favorites = new HashSet<>();
    private List<String> searchHistory = new ArrayList<>();

    public Set<String> getFavorites() {
        return favorites;
    }

    public void setFavorites(Set<String> favorites) {
        this.favorites = favorites;
    }
    
    public void removeFavorite(String favorite) {
        favorites.remove(favorite);
    }

    public List<String> getSearchHistory() {
        return searchHistory;
    }

    public void setSearchHistory(List<String> lastSearches) {
        this.searchHistory = lastSearches;
    }

}
