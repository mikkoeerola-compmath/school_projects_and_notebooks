
package fi.tuni.prog3.weatherapp;

/**
 * Class for handling the weather icons
 * @author Eemeli Pylkkänen
 */
public class SymbolHandler {
    /**
     * Returns path for the symbols .png file
     * @param weatherCode
     * @param iconCode
     * @param cloudiness 0-100%
     * @param rain mm/h
     * @param snow mm/h
     * @return String path for the correct weather symbol
     */
    public static String getSymbol(String weatherCode, String iconCode, 
            int cloudiness, double rain, double snow) {
//        String symbolCodeD0 = iconCode.charAt(2);
        String symbolCodeD1 = "0";
        String symbolCodeD2 = "0";
        String symbolCodeD3 = "0";
        
        if (cloudiness <= 11) {
            symbolCodeD1 = "0";
        } else if ((11 < cloudiness) && (cloudiness <= 25)) {
            symbolCodeD1 = "1";
        } else if ((25 < cloudiness) && (cloudiness <= 50)) {
            symbolCodeD1 = "2";
        } else if ((50 < cloudiness) && (cloudiness <= 84)) {
            symbolCodeD1 = "3";
        } else if ((84 < cloudiness) && (cloudiness <= 100)) {
            symbolCodeD1 = "4";
        }
        
        char weatherCodeD1 = weatherCode.charAt(0);
        char weatherCodeD3 = weatherCode.charAt(2);
        
        switch (weatherCodeD1) {
            case '2': // Thunderstorm
                symbolCodeD2 = "4";
                break;
            case '3': // Drizzle
                symbolCodeD2 = "1";
                break;
            case '5': // Rain
                if (symbolCodeD1.equals("1")) { // Harvinaisissa tilanteissa vähän pilviä mutta sataa silti
                    symbolCodeD1 = "2";
                }
                if (rain <= 2.5) {
                    symbolCodeD2 = "1"; // Light rain
                } else if ((2.5 < rain) && (rain <= 7.5)) {
                    symbolCodeD2 = "2"; // Moderate rain
                } else if (7.5 < rain) {
                    symbolCodeD2 = "3"; // Intense rain
                } 
                break;
            case '6': // Snow
                if (symbolCodeD1.equals("1")) { // Harvinaisissa tilanteissa vähän pilviä mutta sataa silti
                    symbolCodeD1 = "2";
                }
                symbolCodeD3 = "2"; // Snow
                switch (weatherCodeD3) {
                    case '1':
                    case '2':
                    case '3':
                        symbolCodeD3 = "1"; // Sleet
                        break;
                }
                if (snow <= 2.5) {
                    symbolCodeD2 = "1"; // Light rain
                } else if ((2.5 < snow) && (snow <= 7.5)) {
                    symbolCodeD2 = "2"; // Moderate rain
                } else if (7.5 < snow) {
                    symbolCodeD2 = "3"; // Intense rain
                } 
                break;
            case '7': // Atmosphere (fog)
                symbolCodeD1 = "6";
                symbolCodeD2 = "0";
                symbolCodeD3 = "0";
                break;
        }
        
        return String.format("%c%s%s%s.png", 
                iconCode.charAt(2), symbolCodeD1, symbolCodeD2, symbolCodeD3);
    }
}
