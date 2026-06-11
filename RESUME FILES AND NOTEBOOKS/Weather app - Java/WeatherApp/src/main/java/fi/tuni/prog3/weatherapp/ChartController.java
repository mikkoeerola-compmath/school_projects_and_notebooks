package fi.tuni.prog3.weatherapp;

import javafx.fxml.FXML;
import javafx.scene.chart.CategoryAxis;
import javafx.scene.chart.LineChart;
import javafx.scene.chart.NumberAxis;
import javafx.scene.chart.XYChart;
import javafx.scene.control.Button;
import javafx.stage.Stage;

/**
 * Controller class to show chart window.
 *
 * @author Mikko Eerola
 */
public class ChartController {
    
    private HourlyForecast data;
    
    @FXML
    public LineChart<String, Double> lineChart;
    public NumberAxis yAxis;
    public CategoryAxis xAxis;
    public Button backButton;
    
    /**
     * Initializes chart window.
     * 
     * @param hf HourlyForecast the data by hour.
     * @param location Location the data is from.
     */
    public void initialize(HourlyForecast hf, String location) {
        this.data = hf;
        
        XYChart.Series<String, Double> tempSeries = new XYChart.Series<>();
        
        tempSeries.setName("Lämpötila");
        
        for(var elem: data.list) {
            XYChart.Data dataPoint = new XYChart.Data<>(
                    elem.dt_txt.substring(5, 13) ,elem.main.temp-273.15);
            
            tempSeries.getData().add(dataPoint);
        }
        lineChart.getData().add(tempSeries);
        
        lineChart.setTitle(location + ": neljän vuorokauden lämpötilaennuste");
        
      
    }
    
    /**
     * Closes the chart window.
     */
    public void back() {
        Stage stage = (Stage) lineChart.getScene().getWindow();
        stage.close();
    }
}
