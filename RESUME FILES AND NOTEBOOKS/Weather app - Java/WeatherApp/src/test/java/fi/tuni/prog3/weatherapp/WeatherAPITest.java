package fi.tuni.prog3.weatherapp;

import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.AfterAll;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

/**
 * JUnit tests for class WeatherAPI
 * @author Eemeli Pylkkänen
 */
public class WeatherAPITest {
    
    public WeatherAPITest() {
    }
    
    @BeforeAll
    public static void setUpClass() {
    }
    
    @AfterAll
    public static void tearDownClass() {
    }
    
    @BeforeEach
    public void setUp() {
    }
    
    @AfterEach
    public void tearDown() {
    }

    /**
     * Test of lookUpLocation method, of class WeatherAPI.
     */
    @Test
    public void testLookUpLocation() {
        System.out.println("lookUpLocation");
        String loc = "Tampere";
        WeatherAPI instance = new WeatherAPI();
        double[] expResult = {61.4980214, 23.7603118};
        double[] result = instance.lookUpLocation(loc);
        assertArrayEquals(expResult, result);
    }

    /**
     * Test of getCurrentWeather method, of class WeatherAPI.
     */
    @Test
    public void testGetCurrentWeather() {
        System.out.println("getCurrentWeather");
        double lat = 61.4980214;
        double lon = 23.7603118;
        WeatherAPI instance = new WeatherAPI();
        Object result = instance.getCurrentWeather(lat, lon);
        assertTrue(result instanceof CurrentWeather);
    }

    /**
     * Test of getHourlyForecast method, of class WeatherAPI.
     */
    @Test
    public void testGetHourlyForecast() {
        System.out.println("getHourlyForecast");
        double lat = 61.4980214;
        double lon = 23.7603118;
        WeatherAPI instance = new WeatherAPI();
        Object result = instance.getHourlyForecast(lat, lon);
        assertTrue(result instanceof HourlyForecast);
    }
    
    /**
     * Test of getForecast method, of class WeatherAPI.
     */
    @Test
    public void testGetDailyForecast() {
        System.out.println("getDailyForecast");
        double lat = 61.4980214;
        double lon = 23.7603118;
        WeatherAPI instance = new WeatherAPI();
        Object result = instance.getDailyForecast(lat, lon, 16);
        assertTrue(result instanceof DailyForecast);
    }
    
}
