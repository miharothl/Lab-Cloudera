package main.java;

public class Main {


     public static void main(String[] args) {
        System.out.println("Hello World!");

        while (true) {
            System.out.println("Hello World!");

            try
            {
                Thread.sleep(2000);
            }
            catch(InterruptedException e)
            {
                // this part is executed when an exception (in this example InterruptedException) occurs
            }
        }
    }
}
