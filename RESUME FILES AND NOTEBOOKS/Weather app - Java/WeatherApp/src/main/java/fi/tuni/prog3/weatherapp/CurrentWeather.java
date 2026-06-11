
package fi.tuni.prog3.weatherapp;

/**
 * Class for representing the current weather response from the
 * OpenWeatherMap API
 * @author Eemeli Pylkkänen
 */
import com.google.gson.annotations.SerializedName;

public class CurrentWeather {
    
    public static class Coord {
        public double lon;
        public double lat;
    }

    public static class Weather {
        public String id;
        public String main;
        public String description;
        public String icon;
    }

    public static class Main {
        public double temp;
        public double feels_like;
        public double temp_min;
        public double temp_max;
        public int pressure;
        public int humidity;
        public int sea_level;
        public int grnd_level;
    }

    public static class Wind {
        public double speed;
        public int deg;
        public double gust;
    }

    public static class Clouds {
        public int all;
    }

    public static class Sys {
        public int type;
        public int id;
        public String country;
        public long sunrise;
        public long sunset;
    }

    public Coord coord;
    public Weather[] weather;
    public String base;
    public Main main;
    public int visibility;
    public Wind wind;
    @SerializedName("1h")
    public double rain1h = 0;
    public double snow1h = 0;
    public Clouds clouds;
    public long dt;
    public Sys sys;
    public int timezone;
    public int id;
    public String name;
    public int cod;
}



