/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package fi.tuni.prog3.sudoku;

/**
 *
 * @author ckmiee
 */

public class Sudoku {
    private final char[] HYV_C = {'1','2','3','4','5','6','7','8','9',' ','c'};
    
    private char[][] ruudukko = {
        {' ',' ',' ',' ',' ',' ',' ',' ',' '},
        {' ',' ',' ',' ',' ',' ',' ',' ',' '},
        {' ',' ',' ',' ',' ',' ',' ',' ',' '},
        {' ',' ',' ',' ',' ',' ',' ',' ',' '},
        {' ',' ',' ',' ',' ',' ',' ',' ',' '},
        {' ',' ',' ',' ',' ',' ',' ',' ',' '},
        {' ',' ',' ',' ',' ',' ',' ',' ',' '},
        {' ',' ',' ',' ',' ',' ',' ',' ',' '},
        {' ',' ',' ',' ',' ',' ',' ',' ',' '}
    };
    
    public Sudoku() {};
    
    public void set(int i, int j, char c){
        if (i>8 || i<0 || j>8 || j<0) {
            System.out.printf("Trying to access illegal cell (%d, %d)!%n", i,j);
        } else if (!this.check_char(c)){
            System.out.printf("Trying to set illegal "+ 
                    "character %c to (%d, %d)!%n", c,i,j);
        } else {
            this.ruudukko[i][j] = c;
        }
    }
    
    public boolean check() {
        // tarkistetaan ensin rivit
        for (int i = 0; i<9; ++i) {
            if(! check_row(i)) {
                return false;
            }
        }
        
        // tarkistetaan sarakkeet
        for (int i = 0; i<9; ++i) {
            if(! check_col(i)) {
                return false;
            }
        }
        
        // tarkistetaan laatikot

        for(int i = 0; i<9; i+=3) {
            for (int j = 0; j<9; ++j) {
                if(! check_box(i,j)) {
                    return false;
                }
            }
        }
        
        return true;
    }
    
    public void print() {
        System.out.println("#####################################");
        for (int i = 0; i < 9; i++) {
            if (i % 3 == 0 && i > 0) {
                System.out.println("#####################################");
            }

            for (int j = 0; j < 9; j++) {
                if (j % 3 == 0) {
                    System.out.print("#");
                }

                if ((j+1)%3==0 && j > 0) {
                    System.out.print(" " + this.ruudukko[i][j] + " ");
                } else {
                    System.out.print(" " + this.ruudukko[i][j] + " |");
                }
            }
            System.out.println("#");
            if(!((i+1)%3==0)) {
            System.out.println("#---+---+---#---+---+---#---+---+---#");
            }
        }
        System.out.println("#####################################");
    }
    
    private boolean check_char(char c) {
        boolean ans = false;
        for (int i = 0; i<10;++i) {
            if ( c == this.HYV_C[i]) {
                ans = true;
                break;
            }
        }
        return ans;
    }
    
    private boolean check_row(int rivi) {
        for (char c : HYV_C) {
            if (c == ' ') {continue;}
            int count = 0;
            for (int i = 0; i < 9; i++) {
                if (this.ruudukko[rivi][i] == c) {
                    ++count;
                    if (count>1) {
                        System.out.printf("Row %d has multiple %c's!%n",rivi,c);
                        return false;
                    }
                }
            }
        }
        return true;
    }
    private boolean check_col(int sarake) {
        for (char c : HYV_C) {
            if (c == ' ') {continue;}
            int count = 0;
            for (int i = 0; i < 9; i++) {
                if (this.ruudukko[i][sarake] == c) {
                    ++count;
                    if (count>1) {
                        System.out.printf("Column %d has multiple %c's!%n",sarake,c);
                        return false;
                    }
                }
            }
        }
        return true;
    }

    private boolean check_box(int rivi, int sarake){
        for (char c : HYV_C) {
            if (c == ' ') {continue;}
        int count = 0;
        int ruuRiviAlku = (rivi / 3) * 3;
        int ruuSarakeAlku = (sarake / 3) * 3;
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                if (this.ruudukko[ruuRiviAlku + i][ruuSarakeAlku + j] == c) {
                    ++count;
                    if (count>1) {
                        System.out.printf("Block at (%d, %d) has multiple %c's!%n"
                                ,ruuRiviAlku,ruuSarakeAlku,c);
                        return false;
                    }
                }
            }
        }
        }
        return true;
    }
}
