package fi.tuni.prog3.weatherapp;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Map;
import javafx.application.Application;
import javafx.application.Platform;
import javafx.event.ActionEvent;
import javafx.scene.Scene;
import javafx.stage.Stage;
import javafx.fxml.FXMLLoader;
import java.io.IOException;


/**
 * JavaFX Weather Application.
 * 
 * Implements javaFX application that shows weather in searched location.
 */
public class WeatherApp extends Application {

    @Override
    public void start(Stage stage) throws IOException {
        FXMLLoader fxmlLoader = 
                new FXMLLoader(WeatherApp.class.getResource("main.fxml"));
        Scene scene = new Scene(fxmlLoader.load(), 371, 518);
        MainController controller = fxmlLoader.getController();
        controller.initialize();
        stage.setScene(scene);
        stage.setTitle("WeatherApp");
        stage.setResizable(false);
        stage.show();
    }

    public static void main(String[] args) {
        // Tests
//        WeatherAPI api = new WeatherAPI();
//        double[] coordinates = api.lookUpLocation("Tampere");
//        System.out.println(String.format("Latitude: %f, Longitude: %f", coordinates[0], coordinates[1]));
//        
//        CurrentWeather currentWeather = api.getCurrentWeather(coordinates[0], coordinates[1]);
//        System.out.println(currentWeather);
//        
//        HourlyForecast hourlyForecast = api.getHourlyForecast(coordinates[0], coordinates[1]);
//        System.out.println(hourlyForecast);
//
//        DailyForecast dailyForecast = api.getDailyForecast(coordinates[0], coordinates[1], 16);
//        System.out.println(dailyForecast);
//       
//
//        String weatherId = currentWeather.weather[0].id;
//        String weatherIcon = currentWeather.weather[0].icon;
//        int cloudiness = currentWeather.clouds.all;
//        double rain = currentWeather.rain1h;
//        double snow = currentWeather.snow1h;
//
//        System.out.println(SymbolHandler.getSymbol(weatherId, weatherIcon, cloudiness, rain, snow));

        launch();
    }
}