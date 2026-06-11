
package fi.tuni.prog3.weatherapp;

/**
 * Class for representing the daily forecast response from the
 * OpenWeatherMap API
 * @author Eemeli Pylkkänen
 */
import com.google.gson.annotations.SerializedName;
import java.util.List;

public class DailyForecast {
    public City city;
    public String cod;
    public double message;
    public int cnt;
    public List<Forecast> list;

    public static class City {
        public int id;
        public String name;
        public Coord coord;
        public String country;
        public int population;
        public int timezone;
    }

    public static class Coord {
        public double lon;
        public double lat;
    }

    public static class Forecast {
        public long dt;
        public long sunrise;
        public long sunset;
        public Temp temp;
        public FeelsLike feels_like;
        public int pressure;
        public int humidity;
        public List<Weather> weather;
        public double speed;
        public int deg;
        public double gust;
        public int clouds;
        public double pop;
        public double rain = 0;
        public double snow = 0;
        @SerializedName("dt_txt")
        public String dtTxt;
    }

    public static class Temp {
        public double day;
        public double min;
        public double max;
        public double night;
        public double eve;
        public double morn;
    }

    public static class FeelsLike {
        public double day;
        public double night;
        public double eve;
        public double morn;
    }

    public static class Weather {
        public int id;
        public String main;
        public String description;
        public String icon;
    }
}

