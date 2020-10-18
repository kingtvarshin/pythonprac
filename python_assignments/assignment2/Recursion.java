package python_assignments.assignment2;

import java.util.Scanner;

public class Recursion {
    public static void main(String[] args) {
        lexiorder();
    }

    public static void lexiorder() {
        Scanner scn = new Scanner(System.in);
        System.out.println("Print the value n");
        int n = scn.nextInt();
        for(int i=1; i<=9; i++){
            lexirecur(i,n);
        }
        scn.close();
    }
    public static void lexirecur(int i, int n){
        if(i>n){
            return;
        }
        System.out.println(i);
        for(int j=0; j<=9; j++){
            lexirecur(i*10+j,n) ;
        }
    }

    


}