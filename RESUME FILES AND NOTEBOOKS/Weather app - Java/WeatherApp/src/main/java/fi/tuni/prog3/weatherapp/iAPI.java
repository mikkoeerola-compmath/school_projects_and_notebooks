package fi.tuni.prog3.weatherapp;

/**
 * Interface for extracting data from the OpenWeatherMap API.
 */
public interface iAPI {

    /**
     * Returns coordinates for a location.
     * @param loc Name of the location for which coordinates should be fetched.
     * @return double[]: {latitude, longitude}
     */
    public double[] lookUpLocation(String loc);

    /**
     * Returns the current weather for the given coordinates.
     * @param lat The latitude of the location.
     * @param lon The longitude of the location.
     * @return CurrentWeather object
     */
    public CurrentWeather getCurrentWeather(double lat, double lon);

    /**
     * Returns a forecast for the given coordinates.
     * @param lat The latitude of the location.
     * @param lon The longitude of the location.
     * @return HourlyForecast object
     */
    public HourlyForecast getHourlyForecast(double lat, double lon);
    
    /**
     * Returns coordinates for a location.
     * @param lat The latitude of the location.
     * @param lon The longitude of the location.
     * @param cnt Number of forecasted days
     * @return DailyForecast object
     */
    public DailyForecast getDailyForecast(double lat, double lon, int cnt);
}
