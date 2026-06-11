package fi.tuni.prog3.weatherapp;

import java.io.IOException;
import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.scene.Scene;
import javafx.scene.control.Label;
import javafx.stage.Stage;
import javafx.scene.image.Image;
import javafx.scene.image.ImageView;
import java.time.Instant;
import java.time.LocalDateTime;
import java.time.ZoneId;
import java.time.DayOfWeek;
import java.time.format.TextStyle;
import java.util.List;
import java.util.Locale;
import javafx.scene.layout.VBox;

/**
 * FXML Controller class
 * 
 * Class to control weather window events and update the weather information
 *
 * @author Mikko Eerola
 */
public class MainController {

    private final WeatherAPI api = new WeatherAPI();
    private CurrentWeather currentWeather;
    private DailyForecast dailyForecast;
    private HourlyForecast hourlyForecast;
    private String location = "";
    private final String dataFile = "userdata.json";
    private final ReadAndWriteToFile readAndWriteFile = new ReadAndWriteToFile();
    
    // Inject the elements from main.fxml
    @FXML
    public ImageView wIconNow;
    public Label tempNow;
    public Label city;
    public Label highLowNow;
    public Label windNow;
    public Label pressureNow;
    public Label feelslikeNow;
    public Label sunNow;
    
    @FXML
    public Label date1;
    public ImageView wIcon1;
    public Label highLow1;
    public Label add1;
    public Label date2;
    public ImageView wIcon2;
    public Label highLow2;
    public Label add2;
    public Label date3;
    public ImageView wIcon3;
    public Label highLow3;
    public Label add3;
    public Label date4;
    public ImageView wIcon4;
    public Label highLow4;
    public Label add4;
    public Label date5;
    public ImageView wIcon5;
    public Label highLow5;
    public Label add5;
    
    @FXML
    public VBox day1;
    public VBox day2;
    public VBox day3;
    public VBox day4;
    
    @FXML
    public Label gTime1;
    public Label gTime2;
    public Label gTime3;
    public Label gTime4;
    public Label gTime5;
    public Label gTime6;
    public Label gTime7;
    public Label gTime8;
    public Label gTime9;
    public Label gTime10;
    public Label gTime11;
    public Label gTime12;
    public Label gTime13;
    public Label gTime14;
    public Label gTime15;
    public Label gTime16;
    public Label gTime17;
    public Label gTime18;
    public Label gTime19;
    public Label gTime20;
    public Label gTime21;
    public Label gTime22;
    public Label gTime23;
    public Label gTime24;
    
    @FXML
    public ImageView gIcon1;
    public ImageView gIcon2;
    public ImageView gIcon3;
    public ImageView gIcon4;
    public ImageView gIcon5;
    public ImageView gIcon6;
    public ImageView gIcon7;
    public ImageView gIcon8;
    public ImageView gIcon9;
    public ImageView gIcon10;
    public ImageView gIcon11;
    public ImageView gIcon12;
    public ImageView gIcon13;
    public ImageView gIcon14;
    public ImageView gIcon15;
    public ImageView gIcon16;
    public ImageView gIcon17;
    public ImageView gIcon18;
    public ImageView gIcon19;
    public ImageView gIcon20;
    public ImageView gIcon21;
    public ImageView gIcon22;
    public ImageView gIcon23;
    public ImageView gIcon24;
    
    @FXML
    public Label gTemp1;
    public Label gTemp2;
    public Label gTemp3;
    public Label gTemp4;
    public Label gTemp5;
    public Label gTemp6;
    public Label gTemp7;
    public Label gTemp8;
    public Label gTemp9;
    public Label gTemp10;
    public Label gTemp11;
    public Label gTemp12;
    public Label gTemp13;
    public Label gTemp14;
    public Label gTemp15;
    public Label gTemp16;
    public Label gTemp17;
    public Label gTemp18;
    public Label gTemp19;
    public Label gTemp20;
    public Label gTemp21;
    public Label gTemp22;
    public Label gTemp23;
    public Label gTemp24;
    
    @FXML
    public Label gWind1;
    public Label gWind2;
    public Label gWind3;
    public Label gWind4;
    public Label gWind5;
    public Label gWind6;
    public Label gWind7;
    public Label gWind8;
    public Label gWind9;
    public Label gWind10;
    public Label gWind11;
    public Label gWind12;
    public Label gWind13;
    public Label gWind14;
    public Label gWind15;
    public Label gWind16;
    public Label gWind17;
    public Label gWind18;
    public Label gWind19;
    public Label gWind20;
    public Label gWind21;
    public Label gWind22;
    public Label gWind23;
    public Label gWind24;
    
    @FXML
    public Label gRain1;
    public Label gRain2;
    public Label gRain3;
    public Label gRain4;
    public Label gRain5;
    public Label gRain6;
    public Label gRain7;
    public Label gRain8;
    public Label gRain9;
    public Label gRain10;
    public Label gRain11;
    public Label gRain12;
    public Label gRain13;
    public Label gRain14;
    public Label gRain15;
    public Label gRain16;
    public Label gRain17;
    public Label gRain18;
    public Label gRain19;
    public Label gRain20;
    public Label gRain21;
    public Label gRain22;
    public Label gRain23;
    public Label gRain24;
    
    /**
     * Initializes last viewed location and updates the information. By
     * Default opens weather in Tampere.
     */
    public void initialize() {
        try {
            List<String> searchHistory =
                    this.readAndWriteFile.getSearchHistory(dataFile);
            setLocation(searchHistory.get(searchHistory.size()-1));
        } catch (IOException | IndexOutOfBoundsException e) {
            setLocation("Tampere");
        } finally {
            updateWeather();
        }
    }

    /**
     * Set location
     * @param location
     * @return true, if location is found from API. false otherwise 
     */
    public boolean setLocation(String location) {
        if(api.lookUpLocation(location)[0] == -1.0 &
                api.lookUpLocation(location)[1] == -1.0) {
            return false;
        }
        this.location = location;
        return true;
    }

    /**
     * Gets current weather information from API and sets it to variable.
     */
    public void setCurrentWeather() {
        this.currentWeather = api.getCurrentWeather(
                api.lookUpLocation(location)[0], 
                api.lookUpLocation(location)[1]);
    }
    
    /**
     * Gets daily forecast for 5 days from API and sets to variable.
     */
    public void setDailyForecast() {
        this.dailyForecast = api.getDailyForecast(
            api.lookUpLocation(location)[0],
            api.lookUpLocation(location)[1], 5);
    }
    
    /**
     * Gets hourly forecast for 96 hours from API and sets to variable.
     */
    public void setHourlyForecast() {
        this.hourlyForecast = api.getHourlyForecast(
                api.lookUpLocation(location)[0],
                api.lookUpLocation(location)[1]);
    }

    /**
     * Opens and sets up search window from search.fxml. If IOException opening
     * file, doesn't do anything. Attached to MenuItem search.
     */
    @FXML
    public void searchMenu() {
        try {
        Stage stage = (Stage) city.getScene().getWindow();
        FXMLLoader loader = new FXMLLoader(MainController.class.getResource("search.fxml"));
        Scene searchScene = new Scene(loader.load(), 273, 409);
        SearchController controller = loader.getController();
        controller.setLastLocation(location);
        stage.setScene(searchScene);
        } catch (IOException e) {
            System.out.println(e);
        }
    }
    
    /**
     * Adds the current location to the UserData file. Catches IOException but
     * doesn't do anything if the write fails.
     */
    @FXML
    public void setFav() {
        try {
            this.readAndWriteFile.addFavorite(dataFile, this.location);
        } catch (IOException ex) {
            System.out.println(ex);
        }
    }
    
    @FXML
    public void showChart() {
        try {
        Stage stage = new Stage();
        FXMLLoader loader = new FXMLLoader(MainController.class.getResource("chart.fxml"));
        Scene chartScene = new Scene(loader.load(), 600, 400);
        ChartController controller = loader.getController();
        controller.initialize(hourlyForecast, location);
        stage.setScene(chartScene);
        stage.show();
        } catch (IOException e) {
            System.out.println(e);
        }
    }
    
    /**
     * Action to be done if dayForecast1 is pressed.
     */
    @FXML
    public void showHourly1(){
        highlightOff();
        day1.setStyle("-fx-background-color: lightblue;");
        updateWeatherHourly(0);
    }
    
    /**
     * Action to be done if dayForecast2 is pressed.
     */
    public void showHourly2(){
        highlightOff();
        day2.setStyle("-fx-background-color: lightblue;");
        updateWeatherHourly(1);
        
    }
    
    /**
     * Action to be done if dayForecast3 is pressed.
     */
    public void showHourly3(){
        highlightOff();
        day3.setStyle("-fx-background-color: lightblue;");
        updateWeatherHourly(2);
    }
    
    /**
     * Action to be done if dayForecast4 is pressed.
     */
    public void showHourly4(){
        highlightOff();
        day4.setStyle("-fx-background-color: lightblue;");
        updateWeatherHourly(3);
    }
    
    /**
     * Sets the highlight off from every day forecast boxes.
     */
    public void highlightOff() {
        String normalStyle = "-fx-background-color: transparent;";
        day1.setStyle(normalStyle);
        day2.setStyle(normalStyle);
        day3.setStyle(normalStyle);
        day4.setStyle(normalStyle);
    }
    
    /**
     * Updates all weather information fields.
     */
    public void updateWeather() {
        updateWeatherNow();
        updateWeatherDaily();
        updateWeatherHourly(0);
    }
    
    /**
     * Updates current weather information.
     */
    public void updateWeatherNow() {
        this.setCurrentWeather();
        
        city.setText(location);
        
        String weatherId = currentWeather.weather[0].id;
        String weatherIcon = currentWeather.weather[0].icon;
        int cloudiness = currentWeather.clouds.all;
        double rain = currentWeather.rain1h;
        double snow = currentWeather.snow1h;
        setIcon(SymbolHandler.getSymbol(weatherId, weatherIcon,
                cloudiness, rain, snow), wIconNow);
        
        double temp = currentWeather.main.temp;
        String tempSt = formatTemp(temp, true, true);
        this.tempNow.setText(tempSt);
        
        double max = currentWeather.main.temp_max;
        double min = currentWeather.main.temp_min;
        String minmaxSt = formatTemp(min, true, true)+"..."
                +formatTemp(max, true, true);
        this.highLowNow.setText(minmaxSt);
        
        double windSpeed = currentWeather.wind.speed;
        int windDir = currentWeather.wind.deg;
        String wind = formatWind(windSpeed, windDir, true);
        windNow.setText(wind);
        
        int pressure = currentWeather.main.pressure;
        pressureNow.setText(String.format("%d hPa", pressure));
        
        double feelsLike = currentWeather.main.feels_like;
        String feelsLikeSt = formatTemp(feelsLike, true, true);
        feelslikeNow.setText("👤: "+feelsLikeSt);
        
        long sunrise = currentWeather.sys.sunrise;
        long sunset = currentWeather.sys.sunset;
        sunNow.setText("🌅: " + timeStUnix(sunrise, false, false)
                +"-"+timeStUnix(sunset, false, false));
    }
    
    /**
     * Updates all daily forecast fields.
     */
    public void updateWeatherDaily(){
        this.setDailyForecast();
        
        updateOneDay(date1, wIcon1, highLow1, add1, 0);
        updateOneDay(date2, wIcon2, highLow2, add2, 1);
        updateOneDay(date3, wIcon3, highLow3, add3, 2);
        updateOneDay(date4, wIcon4, highLow4, add4, 3);
        updateOneDay(date5, wIcon5, highLow5, add5, 4);
    }
    
    /**
     * Updates one day forecast information.
     * 
     * @param date Label to show date.
     * @param icon ImageView to show weather icon.
     * @param highLow Label to show min max temperature.
     * @param add Label to wind speed and direction.
     * @param day int number of days from today which to show.
     */
    public void updateOneDay(Label date, ImageView icon,
            Label highLow, Label add, int day) {
        long dateTime = dailyForecast.list.get(day).dt;
        date.setText(timeStUnix(dateTime, true, false));
        
        int weatherId = dailyForecast.list.get(day).weather.get(0).id;
        String wIdSt = Integer.toString(weatherId);
        String weatherIcon = dailyForecast.list.get(day).weather.get(0).icon;
        int cloudiness = dailyForecast.list.get(day).clouds;
        double rain = dailyForecast.list.get(day).rain;
        double snow = 0.0;
        setIcon(SymbolHandler.getSymbol(wIdSt, weatherIcon,
                cloudiness, rain, snow), icon);
        
        double max = dailyForecast.list.get(day).temp.max;
        double min = dailyForecast.list.get(day).temp.min;
        highLow.setText(formatTemp(min, false, true)+"/"
                +formatTemp(max, false, true));
        
        double windSpeed = dailyForecast.list.get(day).speed;
        int windDir = dailyForecast.list.get(day).deg;
        String windSt = formatWind(windSpeed, windDir, true);
        add.setText(windSt);
    }
    
    /**
     * Updates hourly forecast.
     * 
     * @param day int number of days from today which to show.
     */
    public void updateWeatherHourly(int day) {
        this.setHourlyForecast();
        
        // Calculate how many hours should we skip from dt moment to show the right hours.
        long firstDt = hourlyForecast.list.get(0).dt;
        Instant instant = Instant.ofEpochSecond(firstDt);
        LocalDateTime dateTime = LocalDateTime.ofInstant(instant,
                ZoneId.systemDefault());
        int hour = dateTime.getHour();
        int hourLeft = 0;
        // if day == 0, we should start from 0 hour and show the next 24h.
        // else show from midnight.
        if(day!=0) {
            hourLeft = 24-hour;
        } else {
            day+=1;
        }
        
        updateOneHour(gTime1, gIcon1, gTemp1, gWind1, gRain1, hourLeft+(day-1)*24);
        updateOneHour(gTime2, gIcon2, gTemp2, gWind2, gRain2, hourLeft+(day-1)*24+1);
        updateOneHour(gTime3, gIcon3, gTemp3, gWind3, gRain3, hourLeft+(day-1)*24+2);
        updateOneHour(gTime4, gIcon4, gTemp4, gWind4, gRain4, hourLeft+(day-1)*24+3);
        updateOneHour(gTime5, gIcon5, gTemp5, gWind5, gRain5, hourLeft+(day-1)*24+4);
        updateOneHour(gTime6, gIcon6, gTemp6, gWind6, gRain6, hourLeft+(day-1)*24+5);
        updateOneHour(gTime7, gIcon7, gTemp7, gWind7, gRain7, hourLeft+(day-1)*24+6);
        updateOneHour(gTime8, gIcon8, gTemp8, gWind8, gRain8, hourLeft+(day-1)*24+7);
        updateOneHour(gTime9, gIcon9, gTemp9, gWind9, gRain9, hourLeft+(day-1)*24+8);
        updateOneHour(gTime10, gIcon10, gTemp10, gWind10, gRain10, hourLeft+(day-1)*24+9);
        updateOneHour(gTime11, gIcon11, gTemp11, gWind11, gRain11, hourLeft+(day-1)*24+10);
        updateOneHour(gTime12, gIcon12, gTemp12, gWind12, gRain12, hourLeft+(day-1)*24+11);
        updateOneHour(gTime13, gIcon13, gTemp13, gWind13, gRain13, hourLeft+(day-1)*24+12);
        updateOneHour(gTime14, gIcon14, gTemp14, gWind14, gRain14, hourLeft+(day-1)*24+13);
        updateOneHour(gTime15, gIcon15, gTemp15, gWind15, gRain15, hourLeft+(day-1)*24+14);
        updateOneHour(gTime16, gIcon16, gTemp16, gWind16, gRain16, hourLeft+(day-1)*24+15);
        updateOneHour(gTime17, gIcon17, gTemp17, gWind17, gRain17, hourLeft+(day-1)*24+16);
        updateOneHour(gTime18, gIcon18, gTemp18, gWind18, gRain18, hourLeft+(day-1)*24+17);
        updateOneHour(gTime19, gIcon19, gTemp19, gWind19, gRain19, hourLeft+(day-1)*24+18);
        updateOneHour(gTime20, gIcon20, gTemp20, gWind20, gRain20, hourLeft+(day-1)*24+19);
        updateOneHour(gTime21, gIcon21, gTemp21, gWind21, gRain21, hourLeft+(day-1)*24+20);
        updateOneHour(gTime22, gIcon22, gTemp22, gWind22, gRain22, hourLeft+(day-1)*24+21);
        updateOneHour(gTime23, gIcon23, gTemp23, gWind23, gRain23, hourLeft+(day-1)*24+22);
        updateOneHour(gTime24, gIcon24, gTemp24, gWind24, gRain24, hourLeft+(day-1)*24+23);
    }
    
    /**
     * Updates one hour.
     * 
     * @param hour Label to show which hour the forecast represents.
     * @param iconIV ImageView to show weather icon.
     * @param tempL Label to show temperature.
     * @param windL Label to show wind speed and direction.
     * @param rainL Label to show rain or snow.
     * @param skip int number of hours from this moment to show the right hour
     */
    public void updateOneHour(Label hour, ImageView iconIV, Label tempL,
            Label windL, Label rainL, int skip) {
        long time = hourlyForecast.list.get(skip).dt;
        hour.setText(timeStUnix(time, false, true));
        
        int id = hourlyForecast.list.get(skip).weather[0].id;
        String idSt = Integer.toString(id);
        String icon = hourlyForecast.list.get(skip).weather[0].icon;
        int clouds = hourlyForecast.list.get(skip).clouds.all;
        double rain;
        if(hourlyForecast.list.get(skip).rain == null) {
            rain = 0;
        } else {
            rain = hourlyForecast.list.get(skip).rain.h1;
        }
        double snow;
        if(hourlyForecast.list.get(skip).snow == null) {
            snow = 0;
        } else {
            snow = hourlyForecast.list.get(skip).snow.h1;
        } 
        setIcon(SymbolHandler.getSymbol(idSt, icon, clouds,
                rain, snow), iconIV);
        
        double temp = hourlyForecast.list.get(skip).main.temp;
        tempL.setText(formatTemp(temp, false, false));
        
        double windSpeed = hourlyForecast.list.get(skip).wind.speed;
        int windDir = hourlyForecast.list.get(skip).wind.deg;
        String wind = formatWind(windSpeed, windDir, false);
        windL.setText(wind);
        
        double maxRainSnow = Double.max(rain, snow);
        rainL.setText(String.format("%.1f", maxRainSnow));
    }
    
    /**
     * Sets weather icon.
     * 
     * @param file String to the image resource.
     * @param iv ImageView to show the icon.
     */
    @FXML
    public void setIcon(String file, ImageView iv) {
        Image wIcon;
        try {
            wIcon = new Image(file);
            iv.setImage(wIcon);
        } catch(IllegalArgumentException e) {
            wIcon = new Image("default.png"); 
            iv.setImage(wIcon);
        }
    }
    
    /**
     * Formating API deafault temparure.
     * 
     * @param temp double temperature to format.
     * @param decimal boolean true if decimals to be shown, false if not.
     * @param unit boolean true if units to be included, false if not.
     * @return String formatted temperature.
     */
    public String formatTemp(double temp, boolean decimal, boolean unit) {
        temp -= 273.15;
        if (decimal) {
            return String.format("%.1f°C", temp);
        } else if (unit){
            return String.format("%.0f°C", temp);
        } else {
            return String.format("%.1f", temp);
        }
    }
    
    /**
     * Formating API default wind.
     * 
     * @param speed double wind speed.
     * @param dir int direction of the wind.
     * @param unit boolean true if units to be included, false if not.
     * @return 
     */
    public String formatWind(double speed, int dir, boolean unit) {
        String arrow;

        // Defining the right arrrow to show direciton.
        if ((dir >= 338 && dir <= 360) || (dir >= 0 && dir <= 22)) {
            arrow = "↓"; // et
        } else if (dir > 22 && dir <= 67) {
            arrow = "↙"; // lo
        } else if (dir > 67 && dir <= 112) {
            arrow = "←"; // lä
        } else if (dir > 112 && dir <= 157) {
            arrow = "↖"; // lu
        } else if (dir > 157 && dir <= 202) {
            arrow = "↑"; // po
        } else if (dir > 202 && dir <= 247) {
            arrow = "↗"; // ko
        } else if (dir > 247 && dir <= 292) {
            arrow = "→"; // it
        } else if (dir > 292 && dir <= 337) {
            arrow = "↘"; // ka
        } else {
            arrow = "tun.suun.";
        }
        
        if(unit) {
            return String.format("%.1f m/s %s", speed, arrow);
        } else {
            return String.format("%.1f %s", speed, arrow);
        }
    }
    
    /**
     * Foramting unix time to needed formats.
     * 
     * @param unixTime long unix time.
     * @param date boolean true if date is to be returned, false if not.
     * @param hourOnly boolean true if only hours to be returned, false if not.
     * @return 
     */
    public String timeStUnix(long unixTime, boolean date, boolean hourOnly) {
        Instant instant = Instant.ofEpochSecond(unixTime);
        LocalDateTime dateTime = LocalDateTime.ofInstant(instant,
                ZoneId.systemDefault());
        int hour = dateTime.getHour();
        int minute = dateTime.getMinute();
        int day = dateTime.getDayOfMonth();
        int month = dateTime.getMonthValue();
        DayOfWeek weekDay = dateTime.getDayOfWeek();
        String st;
        if(date) {
            String lyh = weekDay.getDisplayName(TextStyle.SHORT, Locale.getDefault());
            st = String.format("%s %d.%d", lyh, day, month);
        } else if (!hourOnly) {
            st = String.format("%d.%d", hour, minute);
        } else {
            st = String.format("%d", hour);
        }
        return st;
    }
}
