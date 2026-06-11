/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 */

/**
 *
 * @author ckmiee
 */

import java.util.Scanner;
import java.util.ArrayList;
import java.io.IOException;
import java.util.Collections;

public class Parameters {

    public static void main(String[] args) throws IOException{
        Scanner user = new Scanner(System.in);
        ArrayList<String> paramList = new ArrayList<>();
        
        System.out.println("Parameters:");
        
        String suurin = "";
        
        while (true) {
            String param = user.nextLine();
            if ("".equals(param)) {break;}
            paramList.add(param);
            suurin = (suurin.length() < param.length()) ? param : suurin; 
        }
        
        int num = paramList.size();
        int wid1 = 0;
	
	    while (num != 0) {
		    num = num/10;
		    wid1 +=1;
	    }

        Collections.sort(paramList);
        
        for (int i = 0; i < (wid1 + 2 + suurin.length() + 2 + 3); ++i) {
            System.out.print("#");
        }
        System.out.println();
        
        for (int i = 0; i<paramList.size();++i) {
            System.out.print("#");
            System.out.format(" %"+wid1+"d ", i+1);
            System.out.format("| %-"+suurin.length()+"s #", paramList.get(i));
            System.out.println();
            if (i!=paramList.size()-1) {
            System.out.print("#");
            for (int j = 0; j < wid1+2; ++j) {
                System.out.print("-");
            }
            System.out.print("+");
            for (int j = 0; j<suurin.length()+2;++j) {
                System.out.print("-");
            }
            System.out.println("#");
            }
        }
        
        for (int i = 0; i < (wid1 + 2 + suurin.length() + 2 + 3); ++i) {
            System.out.print("#");
        }
        System.out.println();
        
        
    }
}
