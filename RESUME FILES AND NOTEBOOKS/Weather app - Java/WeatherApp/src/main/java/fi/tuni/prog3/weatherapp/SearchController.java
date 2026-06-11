/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package fi.tuni.prog3.weatherapp;

import java.io.IOException;
import java.util.List;
import javafx.event.ActionEvent;
import javafx.event.EventHandler;
import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.MenuButton;
import javafx.scene.control.MenuItem;
import javafx.scene.control.TextField;
import javafx.scene.input.KeyCode;
import javafx.scene.input.KeyEvent;
import javafx.scene.layout.AnchorPane;
import javafx.scene.layout.VBox;
import javafx.stage.Stage;
import java.util.Set;

/**
 * FXML Controller class
 *
 * @author Mikko Eerola
 */

public class SearchController {
    
    private String lastLocation = "Tampere";
    private final String dataFile = "userdata.json";
    private final ReadAndWriteToFile file = new ReadAndWriteToFile();

    /**
     * Sets the lastLocation.
     * @param lastLocation String last viewed locaiton.
     */
    public void setLastLocation(String lastLocation) {
        this.lastLocation = lastLocation;
    }

    @FXML
    public MenuButton menuFav;

    @FXML
    public TextField searchText;

    @FXML
    public VBox searchBox;
    
    @FXML
    public Button backButton;
    
    @FXML
    public AnchorPane window;
    
    
    @FXML
    public void backClicked(ActionEvent e) throws IOException {
        backMain(lastLocation);
    }
    
    @FXML
    public void enterSearch(KeyEvent k) throws IOException {
        if(k.getCode() == KeyCode.ENTER) {
            backMain(searchText.getText());
        }
    }

    /**
     * Initilizes the favourites and search history. 
     */
    @FXML
    public void initialize() {
        try {
            setFavourites();
            setSearchHistory();
        } catch (IOException ex) {
            System.out.println(ex);
        }
    }

    /**
     * Action to be done if search is pressed.
     * 
     * @throws IOException 
     */
    @FXML
    public void searchLoc() throws IOException {
        String location = searchText.getText();
        searchText.setText("");
        searchText.setPromptText("Hae kaupunkia");
        backMain(location);
    }
    
    /**
     * Goes back to main window if location is found from API. Saves the
     * location to search history.
     * 
     * @param location String weather is shown for this location.
     * @throws IOException 
     */
    @FXML
    public void backMain(String location) throws IOException {
        Stage stage = (Stage) searchText.getScene().getWindow();
        FXMLLoader fxmlLoader = 
                new FXMLLoader(WeatherApp.class.getResource("main.fxml"));
        Scene weatherscene = new Scene(fxmlLoader.load(), 371, 518);
        MainController controller = fxmlLoader.getController();
        boolean isAPlace = controller.setLocation(location);
        if(isAPlace) {
            controller.updateWeather();
            stage.setScene(weatherscene);
            file.addSearchHistory(dataFile, location);
        } else {
            searchText.setText("Paikkaa ei löytynyt");
        }
    }
    
    /**
     * Sets the favourites to the menu.
     * 
     * @throws IOException 
     */
    public void setFavourites() throws IOException {
        Set<String> favourites = file.getFavorites(dataFile);
        for(String fav:favourites) {
            MenuItem menuItem = new MenuItem(fav);
            menuFav.getItems().add(menuItem);
            
            menuItem.setOnAction(event -> {
                try {
                    backMain(fav);
                } catch (IOException ex) {
                    System.out.println(ex);
                }
            });
        }
    }
    
    /**
     * Sets search history to the scrollPane.
     * 
     * @throws IOException 
     */
    public void setSearchHistory() throws IOException {
        List<String> searchHistory = file.getSearchHistory(dataFile);
        for (int i = searchHistory.size()-1; i >= 0; --i) {
            String search = searchHistory.get(i);
            Button but = new Button(search);
            but.setMinWidth(225.0);
            searchBox.getChildren().add(but);
            but.setOnAction(event -> {
                try {
                    backMain(search);
                } catch (IOException ex) {
                    System.out.println(ex);
                }
            });
        }
    }
}
