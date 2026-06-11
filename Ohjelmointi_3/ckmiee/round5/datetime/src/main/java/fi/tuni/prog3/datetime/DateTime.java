/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 */

package fi.tuni.prog3.datetime;

/**
 *
 * @author Omistaja
 */
public class DateTime extends Date {
    private int hour;
    private int minutes;
    private int seconds;
    
    public DateTime(int y, int m, int d, int h, int min, int sec)
    throws DateException {
        super(y,m,d);
        if (LegalTime(h,min,sec)) {
            throw new DateException(String.format("Illegal time "+ 
                    "%02d:%02d:%02d",h,min,sec));
        } else {
            this.hour = h;
            this.minutes = min;
            this.seconds = sec;
        }
    }
    
    public int getHour() {
        return this.hour;
    }

    public int getMinute() {
        return minutes;
    }

    public int getSecond() {
        return seconds;
    }
    
    @Override
    public String toString() {
        return String.format(super.toString() + " %02d:%02d:%02d", this.hour,
                this.minutes,this.seconds);
    }
    
    static boolean LegalTime(int h, int min, int sec) throws DateException {
        return (h<0 || min<0 || sec<0 || h>23 || min>59 || sec>59);
    }
}
