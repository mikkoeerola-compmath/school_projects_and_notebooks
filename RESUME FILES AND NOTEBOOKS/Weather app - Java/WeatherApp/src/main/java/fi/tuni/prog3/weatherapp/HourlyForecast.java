
package fi.tuni.prog3.weatherapp;


/**
 * Class for representing the hourly forecast response from the
 * OpenWeatherMap API
 * @author Eemeli Pylkkänen
 */

import com.google.gson.annotations.SerializedName;
import java.util.List;

public class HourlyForecast {
    public String cod;
    public double message;
    public int cnt;
    public List<Forecast> list;
    public City city;

    public static class Forecast {
        public long dt;
        public Main main;
        public Weather[] weather;
        public Clouds clouds;
        public Wind wind;
        public Rain rain;
        public Snow snow;
        public Sys sys;
        public String dt_txt;
    }

    public static class Main {
        public double temp;
        public double feels_like;
        public double temp_min;
        public double temp_max;
        public int pressure;
        public int sea_level;
        public int grnd_level;
        public int humidity;
        public double temp_kf;
    }

    public static class Weather {
        public int id;
        public String main;
        public String description;
        public String icon;
    }

    public static class Clouds {
        public int all;
    }

    public static class Wind {
        public double speed;
        public int deg;
        public double gust;
    }

    public static class Rain {
        @SerializedName("1h")
        public double h1 = 0;
    }
    
    public static class Snow {
        @SerializedName("1h")
        public double h1 = 0;
    }

    public static class Sys {
        public String pod;
    }

    public static class City {
        public int id;
        public String name;
        public Coord coord;
        public String country;
        public int population;
        public int timezone;
        public long sunrise;
        public long sunset;
    }

    public static class Coord {
        public double lat;
        public double lon;
    }
}


