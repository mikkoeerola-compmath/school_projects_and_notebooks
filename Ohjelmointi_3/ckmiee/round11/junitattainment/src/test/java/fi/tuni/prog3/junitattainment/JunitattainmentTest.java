/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/UnitTests/JUnit5TestClass.java to edit this template
 */
package fi.tuni.prog3.junitattainment;


import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import static org.junit.jupiter.api.Assertions.*;
/*import java.lang.IllegalArgumentException;*/
import java.util.stream.Stream;
import org.junit.jupiter.params.provider.MethodSource;
import org.junit.jupiter.params.provider.Arguments;
import static org.junit.jupiter.params.provider.Arguments.arguments;

/**
 *
 * @author Omistaja
 */
public class JunitattainmentTest {
    
    Attainment testA = new Attainment("testi01", "123", 3);
    
    @Test
    public void testgetGrade() {
        System.out.println("getGrade");
        int expGrade = 3;
        int actual = testA.getGrade();
        assertEquals(expGrade, actual);
    }
    
    @Test
    public void testgetCourseCode() {
        System.out.println("getCourseCode");
        String expCode = "testi01";
        String actual = testA.getCourseCode();
        assertEquals(expCode, actual);
    }
    
    @Test
    public void testgetStudentNumber() {
        System.out.println("getStudentNumber");
        String expNum = "123";
        String actual = testA.getStudentNumber();
        assertEquals(expNum, actual);
    }
    
    @ParameterizedTest
    @MethodSource("stringIntProvider")
    public void exceptionTest(String code, String num, int grade) {
        assertThrows(IllegalArgumentException.class, () -> {
        new Attainment(code, num, grade);}
        );
    }
    
    static Stream<Arguments> stringIntProvider() {
        return Stream.of(
            arguments(null, "123", 4),
            arguments("testi01", null, 4),
            arguments("testi01", "123", 6)
        );
    }
    
    @Test
    public void toStringTest() {
        String expP = "testi01 123 3";
        String actual = testA.toString();
        assertEquals(expP, actual);
    }
    
    @ParameterizedTest
    @MethodSource("attainmentIntProvider")
    public void testCompareTo(Attainment other, int result) {
        boolean ans;
        if(result < 0) {
            ans = testA.compareTo(other) <= result;
        } else if(result > 0) {
            ans = testA.compareTo(other) >= result;
        } else {
            ans = testA.compareTo(other) == 0;
        }
        assertTrue(ans);
    }
    
    static Stream<Arguments> attainmentIntProvider() {
        return Stream.of(
            arguments(new Attainment("testi01","123",3), 0),
            arguments(new Attainment("testi01","12",3), 1),
            arguments(new Attainment("vtesti01","123",3), -1)
        );
    }
    
}
