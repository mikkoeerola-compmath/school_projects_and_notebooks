package fi.tuni.prog3.weatherapp;

import com.google.gson.Gson;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.MalformedURLException;
import java.net.URL;
import java.util.List;
import java.util.Map;


/**
 * Class for extracting data from OpenWeatherMap API
 * @author Eemeli Pylkkänen
 */
public class WeatherAPI implements iAPI {

    private static final String API_KEY = "f313f9599c4283bd06890237f15b12ce"; // Your API key
    private static final String API_URL_CURRENT_WEATHER = 
            "https://api.openweathermap.org/data/2.5/weather?";
    private static final String API_URL_FORECAST_HOURLY = 
            "https://pro.openweathermap.org/data/2.5/forecast/hourly?";
    private static final String API_URL_FORECAST_DAILY = 
            "https://api.openweathermap.org/data/2.5/forecast/daily?";
    private static final String API_URL_LOCATION = 
            "http://api.openweathermap.org/geo/1.0/direct?";

    public WeatherAPI() {
    }
    
    @Override
    public double[] lookUpLocation(String loc) {
        String urlComplete = String.format(API_URL_LOCATION + 
                "q=%s&limit=1&appid=%s", loc, API_KEY);
        URL urlObj;
        try {
            urlObj = new URL(urlComplete);
        } catch (MalformedURLException ex) {
          return null; 
        }
        HttpURLConnection con;
        try {
            con = (HttpURLConnection) urlObj.openConnection();
            con.setRequestMethod("GET");
        } catch (IOException ex) {
            return null;
        }
        BufferedReader in;
        try {
            in = new BufferedReader(new InputStreamReader(con.getInputStream()));
        } catch (IOException ex) {
            return null;
        }

        Gson gson = new Gson();
        
        List<Map<String, Object>> data = gson.fromJson(in, List.class);
        con.disconnect();
        
        if(data.isEmpty()) {
            double[] empty = {-1.0,-1.0};
            return empty;
        }
        
        double lat = (double) data.get(0).get("lat");
        double lon = (double) data.get(0).get("lon");
        double[] ret = {lat, lon};
        
        return ret;
    }

    @Override
    public CurrentWeather getCurrentWeather(double lat, double lon) {
        String urlComplete = String.format(API_URL_CURRENT_WEATHER + 
                "lat=%f&lon=%f&appid=%s", lat, lon, API_KEY);
        URL urlObj;
        try {
            urlObj = new URL(urlComplete);
        } catch (MalformedURLException ex) {
          return null; 
        }
        HttpURLConnection con;
        try {
            con = (HttpURLConnection) urlObj.openConnection();
            con.setRequestMethod("GET");
        } catch (IOException ex) {
            return null;
        }
        BufferedReader in;
        try {
            in = new BufferedReader(new InputStreamReader(con.getInputStream()));
        } catch (IOException ex) {
            return null;
        }
        Gson gson = new Gson();
        
        CurrentWeather data = gson.fromJson(in, CurrentWeather.class);
        con.disconnect();
        return data;
    }

    @Override
    public HourlyForecast getHourlyForecast(double lat, double lon) {
        String urlComplete = String.format(API_URL_FORECAST_HOURLY + 
                "lat=%f&lon=%f&cnt=&appid=%s", lat, lon, API_KEY);
        URL urlObj;
        try {
            urlObj = new URL(urlComplete);
        } catch (MalformedURLException ex) {
          return null; 
        }
        HttpURLConnection con;
        try {
            con = (HttpURLConnection) urlObj.openConnection();
            con.setRequestMethod("GET");
        } catch (IOException ex) {
            return null;
        }
        BufferedReader in;
        try {
            in = new BufferedReader(new InputStreamReader(con.getInputStream()));
        } catch (IOException ex) {
            return null;
        }
        Gson gson = new Gson();
        
        HourlyForecast data = gson.fromJson(in, HourlyForecast.class);
        return data;
    }

    @Override
    public DailyForecast getDailyForecast(double lat, double lon, int cnt) {
        String urlComplete = String.format(API_URL_FORECAST_DAILY + 
                "lat=%f&lon=%f&cnt=%d&appid=%s", lat, lon, cnt, API_KEY);
        URL urlObj;
        try {
            urlObj = new URL(urlComplete);
        } catch (MalformedURLException ex) {
          return null; 
        }
        HttpURLConnection con;
        try {
            con = (HttpURLConnection) urlObj.openConnection();
            con.setRequestMethod("GET");
        } catch (IOException ex) {
            return null;
        }
        BufferedReader in;
        try {
            in = new BufferedReader(new InputStreamReader(con.getInputStream()));
        } catch (IOException ex) {
            return null;
        }
        Gson gson = new Gson();
        
        DailyForecast data = gson.fromJson(in, DailyForecast.class);
        return data;
    }
    
}
