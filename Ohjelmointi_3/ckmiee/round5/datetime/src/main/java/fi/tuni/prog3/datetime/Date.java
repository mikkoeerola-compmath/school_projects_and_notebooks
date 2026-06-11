/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package fi.tuni.prog3.datetime;

/**
 *
 * @author Omistaja
 */

public class Date {
    private int day;
    private int month;
    private int year;
    
    public Date(int y, int m, int d) throws DateException{
        
        if (isLegalDate(d,m,y)) {
            throw new DateException(String.format("Illegal date " +
                   "%02d.%02d.%02d", d, m, y));
        }
        this.day = d;
        this.month = m;
        this.year = y;
    }
    
    public int getYear() {
        return this.year;
    }
    
    public int getMonth() {
        return this.month;
    }
    
    public int getDay() {
        return this.day;
    }
    
    @Override
    public String toString() {
        return String.format("%02d.%02d.%02d",this.day,this.month, this.year);
    }
    
    
    // Käytetään materiaaleissa esiteltyä LegalDate luokan toteutusta. Ei
    // kuitenkaan erillisenä luokkana.
    
    static boolean isLeapYear(int year) {
    // Karkausvuosi: jaollinen 4:llä ja ei jaollinen 100:lla tai jaollinen 400:lla.
    // Javan loogisaritmeettiset operaatiot ja return-lause kuin C-kielessä.
    return (year % 4 == 0) && ((year % 100 != 0) || (year % 400 == 0));
    }

    // Kuukausien päivien määrittämisen voi tehdä monella tavalla. Tässä käytetään
    // taulukkosyntaksin lisähavainnollistamiseksi kaksiulotteista esitäytettyä
    // int-taulukkoa: kullekin kuukaudelle 2-alkioinen alitaulukko, jossa päivien määrä
    // tavallisena ja karkausvuonna (ainoa ero helmikuussa eli toisessa alitaulukossa).
    private static int[][] mDays = {{31, 31}, {28, 29}, {31, 31}, {30, 30}, {31, 31}, {30, 30},
                          {31, 31}, {31, 31}, {30, 30}, {31, 31}, {30, 30}, {31, 31}};

    // Funktio monthDays palauttaa tiedon, kuinka monta päivää kuukaudessa
    // month vuonna year on. Palautusarvo -1 vastaa virheellistä kuukautta.
    static int monthDays(int month, int year) {
       int days = -1;
       if(1 <= month && month <= 12) {
       // Ehdollinen operaattori kuin C-kielessä.
       days = isLeapYear(year) ? mDays[month-1][1] : mDays[month-1][0];
     }
    return days;
    }

    // Funktio isLegalDate tutkii, onko parametrien day, month ja year kuvaama
    // päivämäärä laillinen. Tässä vuosiluvun oletetaan olevan aina laillinen.
    static boolean isLegalDate(int day, int month, int year)
            throws DateException {
    // Tuloksen laskenta on suoraviivaista, koska monthDays
    // palauttaa -1, jos kuukausi on laiton.
       return !((1 <= day) && (day <= monthDays(month, year)));
    }
    
}
