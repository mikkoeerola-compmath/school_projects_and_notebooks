/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Other/File.java to edit this template
 */

/**
 *
 * @author Omistaja
 */

public class Sudoku {
    static char[] HYV_C = {'1','2','3','4','5','6','7','8','9','c',' '};
    
    private char[][] ruudukko;
    
    public Sudoku() {
        for (int i = 0; i<9;++i) {
            char[] rivi = {'c','c','c','c','c','c','c','c','c'};
            this.ruudukko[i]= rivi;
        }
    }
    
    public void set(int i, int j, char c){
        if (i>8 || i<0 || j>8 || j<0) {
            System.out.printf("Trying to access illegal cell (%d, %d)!%n", i,j);
        } else if (Sudoku.check_char(c)){
            System.out.printf("Trying to set illegal"+ 
                    "character %c to (%d, %dj)!%n", c,i,j);
        } else {
            this.ruudukko[i][j] = c;
        }
    }
    
    public boolean check() {
        // tarkistetaan ensin rivit
        for (char c : HYV_C) {
            if(c==' '|| c=='c') {continue;}
            for (int i = 0; i<9; ++i) {
                if(! check_row_for(i, c)) {
                    System.out.printf("Row %d has multiple %c's!%n",i,c);
                    return false;
                } 
            }
        }
        
        // tarkistetaan sarakkeet
        for (char c : HYV_C) {
            if(c==' '|| c=='c') {continue;}
            for (int i = 0; i<9; ++i) {
                if(! check_col_for(i, c)) {
                    System.out.printf("Column %d has multiple %c's!%n",i,c);
                    return false;
                } 
            }
        }
        
        // tarkistetaan laatikot
        for (char c : HYV_C) {
            if(c==' ' || c=='c') {continue;}
            for(int i = 0; i<9; i+=3) {
                for (int j = 0; j<9; j+=3) {
                    if(! check_box_for(i,j,c)) {
                        System.out.printf("Block at (%d, %d) has multiple" + 
                                " %c's!%n",i,j,c);
                        return false;
                    } 
                }
            }
        }
        return true;
    }
    
    public void print() {
        System.out.println("#######################");
        for (int i = 0; i < 9; i++) {
            if (i % 3 == 0 && i > 0) {
                System.out.println("#-----+-----+-----#");
            }

            for (int j = 0; j < 9; j++) {
                if (j % 3 == 0 && j > 0) {
                    System.out.print("| ");
                }

                if (ruudukko[i][j] == 0) {
                    System.out.print(". ");
                } else {
                    System.out.print(ruudukko[i][j] + " ");
                }
            }
            System.out.println("#");
        }
        System.out.println("#######################");
    }
    
    static boolean check_char(char c) {
        boolean ans = false;
        for (int i = 0; i<9;++i) {
            if ( c != HYV_C[i]) {
                ans = true;
                break;
            }
        }
        return ans;
    }
    
    private boolean check_row_for(int rivi, char c) {
        int count = 0;
        for (int i = 0; i < 9; i++) {
            if (this.ruudukko[rivi][i] == c) {
                ++count;
                if (count>1) {
                    return false;
                }
            }
        }
        return true;
    }
    private boolean check_col_for(int sarake, char c) {
        int count = 0;
        for (int i = 0; i < 9; i++) {
            if (this.ruudukko[i][sarake] == c) {
                ++count;
                if (count>1) {
                    return false;
                }
            }
        }
        return true;
    }

    private boolean check_box_for(int rivi, int sarake, char c){
        int count = 0;
        int ruuRiviAlku = (rivi / 3) * 3;
        int ruuSarakeAlku = (sarake / 3) * 3;
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                if (this.ruudukko[ruuRiviAlku + i][ruuSarakeAlku + j] == c) {
                    ++count;
                    if (count>1) {
                        return false;
                    }
                }
            }
        }
        return true;
    }
}

